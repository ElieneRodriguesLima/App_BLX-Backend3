"""Nova coluna Tamanhos

Revision ID: 02412e4cc097
Revises: a30fd8715ecb
Create Date: 2021-05-04 15:01:18.289575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02412e4cc097'
down_revision = 'a30fd8715ecb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_usuario_id', table_name='usuario')
    op.drop_table('usuario')
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    op.create_table('usuario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('senha', sa.VARCHAR(), nullable=True),
    sa.Column('telefone', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_usuario_id', 'usuario', ['id'], unique=False)
    # ### end Alembic commands ###
