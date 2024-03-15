"""add foreign-key to posts table

Revision ID: 09d69a06136d
Revises: 8891327f7aba
Create Date: 2024-03-15 16:07:39.896266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09d69a06136d'
down_revision: Union[str, None] = '8891327f7aba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_pk', source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_pk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
