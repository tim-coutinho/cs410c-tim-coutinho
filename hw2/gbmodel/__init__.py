# model_backend = 'pylist'
model_backend = 'dict'
# model_backend = 'sqlite3'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'dict':
    from .model_dict import model
elif model_backend == 'pylist':
    from .model_pylist import model
else:
    raise ValueError('No appropriate databackend configured.')


def get_model():
    return model()
