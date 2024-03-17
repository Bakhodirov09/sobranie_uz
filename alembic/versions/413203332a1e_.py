"""empty message

Revision ID: 413203332a1e
Revises: 16be496d50da
Create Date: 2024-03-13 17:32:38.034673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '413203332a1e'
down_revision: Union[str, None] = '16be496d50da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curer_orders', sa.Column('latitude', sa.String(), nullable=True))
    op.add_column('curer_orders', sa.Column('longitude', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('curer_orders', 'longitude')
    op.drop_column('curer_orders', 'latitude')
    # ### end Alembic commands ###