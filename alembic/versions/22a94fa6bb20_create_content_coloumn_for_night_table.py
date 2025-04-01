"""create content coloumn for night table

Revision ID: 22a94fa6bb20
Revises: a99b71f866fc
Create Date: 2025-04-01 11:00:44.397405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22a94fa6bb20'
down_revision: Union[str, None] = 'a99b71f866fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('contact_number', sa.Integer, nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'contact_number')
