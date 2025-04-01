"""create posts table

Revision ID: a99b71f866fc
Revises: 
Create Date: 2025-04-01 10:48:56.336878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a99b71f866fc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('night', sa.Column('id', sa.Integer, nullable = False, primary_key = True), sa.Column('title', sa.String, nullable = False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('night')
