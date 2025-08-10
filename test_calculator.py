import pytest
from calculator import add


class TestAddFunction:
    """测试add函数的测试类"""
    
    def test_add_positive_numbers(self):
        """测试正数相加"""
        assert add(5, 3) == 8
        assert add(100, 200) == 300
        assert add(999, 1) == 1000
    
    def test_add_negative_numbers(self):
        """测试负数相加"""
        assert add(-5, -3) == -8
        assert add(-100, -200) == -300
        assert add(-999, -1) == -1000
    
    def test_add_mixed_numbers(self):
        """测试正负数混合相加"""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(100, -50) == 50
        assert add(-100, 50) == -50
    
    def test_add_with_zero(self):
        """测试与零相加"""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5
        assert add(0, -5) == -5
    
    def test_add_boundary_values(self):
        """测试边界值"""
        # 大整数
        assert add(999999999, 1) == 1000000000
        assert add(-999999999, -1) == -1000000000
        
        # 浮点数
        assert add(3.14, 2.86) == 6.0
        assert add(-3.14, -2.86) == -6.0
        assert add(3.14, 0) == 3.14
    
    def test_add_commutative_property(self):
        """测试加法交换律"""
        assert add(5, 3) == add(3, 5)
        assert add(-5, 3) == add(3, -5)
        assert add(0, 100) == add(100, 0)
    
    def test_add_associative_property(self):
        """测试加法结合律"""
        # (a + b) + c = a + (b + c)
        a, b, c = 5, 3, 2
        assert add(add(a, b), c) == add(a, add(b, c))
        
        a, b, c = -5, 3, -2
        assert add(add(a, b), c) == add(a, add(b, c))
    
    def test_add_identity_property(self):
        """测试加法恒等性"""
        # a + 0 = a
        assert add(5, 0) == 5
        assert add(-5, 0) == -5
        assert add(0, 0) == 0
    
    def test_add_large_numbers(self):
        """测试大数相加"""
        large_num = 10**15
        assert add(large_num, 1) == large_num + 1
        assert add(large_num, -1) == large_num - 1
    
    def test_add_small_decimals(self):
        """测试小数相加"""
        assert add(0.1, 0.2) == pytest.approx(0.3, rel=1e-10)
        assert add(0.001, 0.002) == pytest.approx(0.003, rel=1e-10)
        assert add(-0.1, -0.2) == pytest.approx(-0.3, rel=1e-10)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
