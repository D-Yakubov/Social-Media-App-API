"""add content column to posts table

Revision ID: 0d48298faf40
Revises: a236d23bee8a
Create Date: 2024-03-14 17:41:24.302814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d48298faf40'
down_revision: Union[str, None] = 'a236d23bee8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
