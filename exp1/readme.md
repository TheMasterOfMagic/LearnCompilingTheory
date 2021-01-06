为明确讨论范围，特定义以下规范：
- Operator：通常意义上的`(`、`)`、`|`与`*`
- Operand：可打印字符中除了Operator与`_`以外的部分
- 正则式：由Operator或Operand构成的长度大于0且保证合法的通常意义上的正则式
- 待匹配串：由Operand构成且长度大于0的通常意义上的字符串
- NFA：有起点、终点，边有符号的有向图。边上的符号可以为Operand或空（程序中以`_`代替）

# 最终目标

实现程序，实现根据给定正则式检测待匹配串是否完全匹配。

## 输入

若干行，每一行格式为`正则式 待匹配串`

## 输出

若匹配则输出`T`, 否则输出`F`

## 示例

1.
    输入
    ```
    a a
    a b
    ab ab
    ab a
    ab b
    ab abc
    a|b a
    a|b b
    a|b c
    a* a
    a* aaaaaaaaaaaa
    ```
    输出
    ```
    TFTFFFTFFTF
    ```

# 子目标

- [exp1-1 手动构造NFA与NFA的序列化](./exp1-1)
- [exp1-2 NFA的反序列化及and、or与closure运算](./exp1-2)
- exp1-3 将正则式转化为NFA
- exp1-4 手动构造DFA与DFA的反序列化
- exp1-5 将NFA转化为DFA
- exp1-6 最小化DFA及检测待匹配串
