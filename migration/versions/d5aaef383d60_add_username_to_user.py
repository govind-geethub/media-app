"""add username to user

Revision ID: d5aaef383d60
Revises: 
Create Date: 2026-10-12 12:34:43.656312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5aaef383d60'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "user",
        sa.Column("username", sa.String(length=50), nullable=True)
    )

    op.create_index(
        "ix_user_username",
        "user",
        ["username"],
        unique=True
    )

    op.execute("""
        UPDATE "user"
        SET username = 'user_' || replace(id, '-', '')
        WHERE username IS NULL
    """)


def downgrade() -> None:
    op.drop_index("ix_user_username", table_name="user")
    op.drop_column("user", "username")