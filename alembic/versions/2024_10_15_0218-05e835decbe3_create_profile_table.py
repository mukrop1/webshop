"""Create profile table

Revision ID: 05e835decbe3
Revises: 7919de959f00
Create Date: 2024-10-15 02:18:45.738022

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "05e835decbe3"
down_revision: Union[str, None] = "7919de959f00"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("first_name", sa.String(length=45), nullable=True),
        sa.Column("last_name", sa.String(length=45), nullable=True),
        sa.Column("sex", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profiles")
    # ### end Alembic commands ###
