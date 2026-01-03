from src.PrintCreationMixin import PrintCreationMixin


def test_mixin():
    class Test(PrintCreationMixin):
        def __init__(self, a, b):
            super().__init__(a, b)

    import io, sys

    out = io.StringIO()
    sys.stdout = out
    Test(1, 2)
    sys.stdout = sys.__stdout__

    assert "Test(1, 2)" in out.getvalue()
