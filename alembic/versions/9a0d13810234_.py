"""empty message

Revision ID: 9a0d13810234
Revises: 
Create Date: 2024-03-13 07:06:01.044600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a0d13810234'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('basket',
    sa.Column('product', sa.String(), nullable=True),
    sa.Column('menu_name', sa.String(), nullable=True),
    sa.Column('miqdor', sa.Integer(), nullable=True),
    sa.Column('narx', sa.BigInteger(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True)
    )
    op.create_table('curers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fast_food_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu', sa.String(), nullable=True),
    sa.Column('food_name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filial_admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('which_filial', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filial_name', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('lang', sa.String(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('locations',
    sa.Column('location_name', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True)
    )
    op.create_table('logo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_picture', sa.String(), nullable=True),
    sa.Column('menu_name', sa.String(), nullable=True),
    sa.Column('lang', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ordering',
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True)
    )
    op.create_table('payments',
    sa.Column('payment_name', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True)
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('lang', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('payments')
    op.drop_table('ordering')
    op.drop_table('menu')
    op.drop_table('logo')
    op.drop_table('locations')
    op.drop_table('history_buys')
    op.drop_table('filials')
    op.drop_table('filial_admins')
    op.drop_table('fast_food_menu')
    op.drop_table('curers')
    op.drop_table('basket')
    op.drop_table('admins')
    # ### end Alembic commands ###