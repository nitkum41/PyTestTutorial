class TestClass:
    def test_one(self):
        x='hello'
        assert 'h' in x
    def test_two(self):
        x='hello'
        assert hasattr(x,"check")
