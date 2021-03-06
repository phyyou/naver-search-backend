"""empty message

Revision ID: 6cce47075cba
Revises: 
Create Date: 2021-10-14 07:14:30.743740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cce47075cba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_search_id'), 'search', ['id'], unique=False)
    op.create_index(op.f('ix_search_keyword'), 'search', ['keyword'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_search_keyword'), table_name='search')
    op.drop_index(op.f('ix_search_id'), table_name='search')
    op.drop_table('search')
    # ### end Alembic commands ###
