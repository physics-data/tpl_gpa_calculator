# GPA Calculator

Template for the first project of Big Data in Physics course.

## 问题背景

芃芃是华清大学计算机系的一名学生，成绩十分优秀。最近，学校进行了 GPA 改革。他想知道改革以后自己的 GPA 到底变化了多少，但是教务系统由于某些原因好像没能跟上步伐。虽然手算是一种方式，但是芃芃选的课实在是**太多了**……因此他向你求助，希望你能够帮他计算出他的 GPA。

## 问题描述

你需要编写一个 Python 程序完成 GPA 的计算。具体来说，你需要填充项目中的 `gpa_calculator.py`，并完成以下功能：

### 指定输入输出文件

你的程序需要能以以下方式运行：

```bash
python3 gpa_calculator.py input_file output_file
```

其中 `input_file` 是输入文件名，`output_file` 是输出文件名。提示：你可以从 `sys` 包中的 `sys.argv` 数组中获取程序的运行参数。

### 根据指定的格式计算每学期 GPA

程序提供的输入文件有多行，每一个**非空行**的格式如下：

```
12090043	军事理论与技能训练	3	B+	3.6	2016-夏
```

即每一行由 6 列组成，每列之间的分隔符是制表符 `'\t'`，你需要进行切分。第一列为课程号，第二列为课程名，第三列为课程学分，第四列为等级，第五列为对应（新）绩点，最后一列为学期名称。

你需要根据这些信息，汇总计算在新、老两种算法下，芃芃每一个学期的 GPA（也就是说，具有相同学期名称的课程需要归类在一起计算），并以每学期一行的格式输出如下：

```
学期名 课程数量 该学期总学分 该学期总GPA学分 GPA（老） GPA（新）
```

关于等级到绩点的映射可参见附录，我们保证所有的等级字段都在其中出现。在计算课程数量时，**需要统计所有的课程（包括不计入 GPA 的课程，无论其等级与状态）**。如果某一学期 GPA 学分为 0，**请将两个 GPA 都输出为 `-1.00`**（样例中的 `2019-春` 学期即为此情况）。

输出的五个字段中使用空格分隔，行末不要有多余的空格。两个 GPA 都需要四舍五入到两位小数，如果不足请补充零。此外，为方便比较，请根据**学期在输入文件中第一次出现的顺序**进行输出。

### 计算总 GPA

在完成上述的任务后，请在文件的最后一行输出如下的内容：

```
学期数量 总课程数量 总学分 总GPA学分 GPA（老） GPA（新）
```

其中对于课程数量和学分的统计、GPA 的计算与输出格式要求与上面相同。我们保证，输入中不会出现总 GPA 学分为 0 的情况。

## 样例与评测

我们提供了一个样例 `examples/gpa.in` 和对应结果 `examples/gpa.out`。你也可以运行 `grader.py` 在样例上对你的代码进行评测。

事实上，输入文件的格式即为 info 上“学习-中文成绩单”栏目的数据格式。你可以直接选中其中的表格部分复制到一个文本文件中，用来测试你的程序。

## 提醒

下面是一些关于解题的提醒：

1. 输入文件中，同一学期的课程未必连续出现，学期名称也未必是例子中的格式。
2. 输入文件中，任何位置都可能有多余的空行。
3. 在计算 GPA 时，你可以将其转换为整数（如先`* 10`），而非使用浮点数运算，以获得更高的精确度。
4. 在最终评测时，将会使用规模更大的随机生成的数据，请注意程序的普适性、鲁棒性与效率。

你可能需要使用 Python 中的 `dict` 等工具来帮助你解决这一问题。

## 附录：GPA 与等级的映射关系


| 等级 | 绩点（老） | 绩点（新） |
|------|------------|------------|
| A+   | 4.0        | 4.0        |
| A    | 4.0        | 4.0        |
| A-   | 3.7        | 4.0        |
| B+   | 3.3        | 3.6        |
| B    | 3.0        | 3.3        |
| B-   | 2.7        | 3.0        |
| C+   | 2.3        | 2.6        |
| C    | 2.0        | 2.3        |
| C-   | 1.7        | 2.0        |
| D+   | 1.3        | 1.6        |
| D    | 1.0        | 1.3        |
| F    | 0.0        | 0.0        |

此外，还有以下等级不计入 GPA 的计算：`EX`（免修）, `W`（退课）, `I`（缓考）, `P`（通过），`***`（尚未公布）。

等级到绩点的转换可以用多种方法实现，比如定义一个函数，或者使用 `dict` 等工具。你可以自行思考，以获得最高的效率。

根据当前学校的约定，在成绩单中相同课程可能重复出现，你无需对此进行特别处理，直接对于每一行都进行计算即可。
