"""Added is_active to Microchips

Revision ID: ddbcfc0ade91
Revises: 
Create Date: 2024-10-27 15:18:35.212296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddbcfc0ade91'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('microchips', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('microchips', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
