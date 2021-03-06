"""Adicionado Usuario e Relacionamento

Revision ID: f956e3f7ded0
Revises: 02412e4cc097
Create Date: 2021-05-04 16:13:52.761727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f956e3f7ded0'
down_revision = '02412e4cc097'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_usuario', 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario', type_='foreignkey')

    # ### end Alembic commands ###
