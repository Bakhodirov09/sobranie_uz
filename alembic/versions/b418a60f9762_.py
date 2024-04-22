"""empty message

Revision ID: b418a60f9762
Revises: 5b951f7771c2
Create Date: 2024-04-21 01:51:57.383254

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b418a60f9762'
down_revision: Union[str, None] = '5b951f7771c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history_buys',
    sa.Column('number', sa.BigInteger(), nullable=True),
    sa.Column('product', sa.String(), nullable=True),
    sa.Column('miqdor', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('bought_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('payment_method', sa.String(), nullable=True),
    sa.Column('payment_status', sa.String(), nullable=True),
    sa.Column('go_or_order', sa.String(), nullable=True),
    sa.Column('which_filial', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history_buys')
    # ### end Alembic commands ###