"""empty message

Revision ID: dfc0fb1468d2
Revises: 67cbe96f7d59
Create Date: 2022-07-27 06:27:37.290743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc0fb1468d2'
down_revision = '67cbe96f7d59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('website', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'website')
    # ### end Alembic commands ###
