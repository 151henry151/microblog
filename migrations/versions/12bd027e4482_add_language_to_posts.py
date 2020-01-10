"""add language to posts

Revision ID: 12bd027e4482
Revises: ae346256b650
Create Date: 2020-01-09 20:42:56.815439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12bd027e4482'
down_revision = 'ae346256b650'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
