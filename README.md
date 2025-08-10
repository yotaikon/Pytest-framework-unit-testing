
# Pytest 单元测试示例

这个项目展示了如何使用 pytest 框架为 `add` 函数编写全面的单元测试。

## 提示词：def add(a, b): return a + b   请用 pytest 框架生成单元测试，要覆盖正数、负数、零的情况，包括边界值。

## 项目结构

```
pytest框架单元测试/
├── calculator.py          # 包含 add 函数的模块
├── test_calculator.py     # pytest 测试文件
├── requirements.txt       # 项目依赖
└── README.md             # 项目说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行测试

### 运行所有测试
```bash
pytest
```

### 运行测试并显示详细信息
```bash
pytest -v
```

### 运行测试并显示输出
```bash
pytest -s
```

### 运行特定测试文件
```bash
pytest test_calculator.py
```

### 运行特定测试方法
```bash
pytest test_calculator.py::TestAddFunction::test_add_positive_numbers
```

## 测试覆盖范围

测试覆盖了以下情况：

1. **正数相加** - 测试各种正数组合
2. **负数相加** - 测试各种负数组合  
3. **正负数混合** - 测试正负数的混合运算
4. **零值处理** - 测试与零的运算
5. **边界值测试** - 测试大数、小数等边界情况
6. **数学性质** - 测试交换律、结合律、恒等性
7. **大数运算** - 测试大整数的处理
8. **小数精度** - 测试浮点数的精度处理

## 测试结果示例

运行 `pytest -v` 应该会看到类似以下的输出：

```
test_calculator.py::TestAddFunction::test_add_positive_numbers PASSED
test_calculator.py::TestAddFunction::test_add_negative_numbers PASSED
test_calculator.py::TestAddFunction::test_add_mixed_numbers PASSED
...
```

所有测试都应该通过，表明 `add` 函数在各种情况下都能正确工作。
