# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    # don't do anything if first installation of the module
    if openupgrade.table_exists(env.cr, "deposit_slip"):
        openupgrade.logged_query(
            env.cr,
            """
            ALTER TABLE deposit_slip
            ADD COLUMN warehouse_id integer
            """,
        )
        # set warehouse from picking
        openupgrade.logged_query(
            env.cr,
            """
                UPDATE deposit_slip
                SET warehouse_id = foo.warehouse_id
                FROM (
                    SELECT DISTINCT ON (deposit_slip_id) t.warehouse_id,
                                                         p.deposit_slip_id
                    FROM stock_picking p
                    JOIN stock_picking_type t ON t.id = p.picking_type_id
                    WHERE p.deposit_slip_id IS NOT NULL
                ) as foo
                WHERE foo.deposit_slip_id = deposit_slip.id
            """,
        )
