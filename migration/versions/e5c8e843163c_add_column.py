"""add column

Revision ID: e5c8e843163c
Revises: 69174a687505
Create Date: 2022-12-14 18:00:21.520052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c8e843163c'
down_revision = '69174a687505'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nft_pr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=30), nullable=False),
    sa.Column('image_URL', sa.String(length=100), nullable=True),
    sa.Column('buy_token_name', sa.String(length=5), nullable=True),
    sa.Column('chain_name', sa.String(length=30), nullable=True),
    sa.Column('floor_price_BT', sa.DECIMAL(), nullable=True),
    sa.Column('BT_price', sa.DECIMAL(), nullable=True),
    sa.Column('earn_token_name', sa.String(length=5), nullable=True),
    sa.Column('ET_price', sa.DECIMAL(), nullable=True),
    sa.Column('last_updated', sa.DATETIME(), nullable=True),
    sa.Column('earn_rate_ET', sa.DECIMAL(), nullable=True),
    sa.Column('contract_address', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_nft_pr_id'), 'nft_pr', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nft_pr_id'), table_name='nft_pr')
    op.drop_table('nft_pr')
    # ### end Alembic commands ###
