"""removing the non nullable attributes for the results table 

Revision ID: 65000b0d4f35
Revises: 3c70c83e90cb
Create Date: 2023-10-05 09:54:19.651583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65000b0d4f35'
down_revision = '3c70c83e90cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('results', schema=None) as batch_op:
        batch_op.alter_column('secondattempt',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('thirdattempt',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('finalattempt',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('results', schema=None) as batch_op:
        batch_op.alter_column('finalattempt',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('thirdattempt',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('secondattempt',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###
