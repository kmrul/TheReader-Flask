"""Membership migrations

Revision ID: e5c0e4587aee
Revises: 2e22cfd6343b
Create Date: 2020-08-28 03:10:58.533305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c0e4587aee'
down_revision = '2e22cfd6343b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('membership',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('post_limit', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_membership_created_date'), 'membership', ['created_date'], unique=False)
    op.create_index(op.f('ix_membership_updated_date'), 'membership', ['updated_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_membership_updated_date'), table_name='membership')
    op.drop_index(op.f('ix_membership_created_date'), table_name='membership')
    op.drop_table('membership')
    # ### end Alembic commands ###
