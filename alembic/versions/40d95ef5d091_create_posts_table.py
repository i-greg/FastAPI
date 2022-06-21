"""create posts table

Revision ID: 40d95ef5d091
Revises: 
Create Date: 2022-06-18 15:44:16.327602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40d95ef5d091'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
