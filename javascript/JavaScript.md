# JavasCript

### Values and Variables

- 变量
- 常量
- 基本数据类型
- 字符串
- 数组

变量

```js
# 声明变量
let num = 10
console.log(num)
```

常量

```js
# 声明常量
const uname = lesen
console.log(uname)
```

基本数据类型

- String
- Number
- Boolean
- Undefined
- Null

转换数据类型

```js
# + 两边只要有一个字符串,就都会转换成字符串
# -*/等会把数据转换成数字类型
# 隐式转换
let num = + '123'
console.log(num)
$ 123
# 显示转换
let num = Number('123')
# 取整数
console.log(parseInt('12.3px'))
$ 12
# 取小数
console.log(parseFloat('12.3px'))
$ 12.3
```

### Object

- 对象(object):JavaScript的一种数据类型

- 可以理解为是一种无序的数据集合,注意数组是有序的数据集合
- 用来描述某个事物,例如描述一个人

对象的使用

```js
let 对象名 = {
    属性名:属性值,
    方法名:函数
}
//对象由属性和方法组成
```

增删改查

语法:对象名.属性

```js
let person = {
    uname: 'lesen',
    age: 18,
    gender: 'male'
}
//查
console.log(person.uname)
$ lesen
//标准的查
console.log(person['uname'])
//改
person.age = 20
$ 20
//增
person.hobby = 'baskteball'
```

对象的方法

```js
let person = {
    uname: 'lesen',
    sum: (x, y) => {
        console.log(x + y)
    }
}
person.sum(1, 2)
```

遍历对象

```js
let person = {
    uname: 'lesen',
    age: 18,
    gender: 'male'
}
for (let k in person) {
    console.log(person.uname)
    console.log(person[k])//k的值是'uname', 'age', 'gender'
}
```

内置对象

Math

```js
//属性
console.log(Math.PI)
//方法
//ceil 向上取整
console.log(Math.ceil(1.1))	$ 2
//floor 乡下取整
console.log(Math.floor(1.1)) $ 1
//round 四舍五入
console.log(Math.roud(1.5))	$ 2
```

随机数

`Math.random()`是[0-1)的数

```js
//0-10的整数
Math.floor(Math.random()*(10+1))
//n-m的随机数
Math.floor(Math.random()*(m - n + 1)) + n
//在数组中随机取
let arr = ['red', 'pink', 'green']
let random = Math.floor(Math.random()*arr.length)
console.log(arr[random])
```

猜数字案例

随机生存1-10之间的数字,用户输入一个数字

```js
let random = Math.floor(Math.random() * 10 + 1)
let guess = +prompt('请输入一个数字');
while (true) {
  if (guess > random) {
    alert(`你输入的数字是${guess},数字大了`)
    guess = +prompt('请输入一个数字');
  } else if (guess < random) {
    alert('数字小了')
    guess = +prompt(`你输入的数字是${guess},数字小了`);
  } else {
    alert(`你输入的数字是${guess},猜对了`)
    break;
  }
}
```

### Calculate

运算符

- 赋值运算符
- 比较运算符
- 一元运算符
- 逻辑运算符
- 运算符优先级

赋值运算符

```js
let num = 10 #只能给变量赋值
num += 1	# 等于 num = num + 1
```

一元运算符

```js
let i = 1;
console.log(++1)	#2
let i = 1;
console.log(i++)	#2
```

比较运算符

```js
let i = 10
console.log(i < 11);	# true
console.log(i > 11);	# false
```

逻辑运算符

| 符号 | 名称   | 日常读法 | 特点                              | 口诀          |
| ---- | ------ | -------- | --------------------------------- | ------------- |
| &&   | 逻辑与 | 并且     | 符号两边都为true;结果才为true     | 一假则假      |
| \|\| | 逻辑或 | 或者     | 符号两边有一个为true;结果就为true | 一真则真      |
| !    | 逻辑非 | 取反     | true变为false;false变为true       | 真变假,假变真 |

运算符优先级

| 优先级 | 运算符     | 顺序          |
| ------ | ---------- | ------------- |
| 1      | 小括号     | ()            |
| 2      | 一元运算符 | ++ -- !       |
| 3      | 算术运算符 | 先*/%后+-     |
| 4      | 关系运算符 | > >= < <=     |
| 5      | 相等运算符 | == != === !== |
| 6      | 逻辑运算符 | 先&& 后\|\|   |
| 7      | 赋值运算符 | =             |
| 8      | 逗号运算符 | ,             |

### 分支语句

if分支语句

```js
if (true) {
	console.log('This is true')
}
---------------
if (true) {
	console.log('This is true')
} else {
	console.log('This is false')
}
--------------
if (条件) {
	执行1
} else if (条件) {
	执行2
} else {
	执行3
}
```

三元运算符

比if双分支更简单的写法, `?`和`:`配合使用

```js
let num1 = +prompt('输入第一个数');
let num2 = +prompt('输入第二个数');
num1 > num2 ? alert(`最大的数是${num1}`) : alert(`最大的数是${num2}`)
```

switch语句

```js
let num1 = +prompt('num1');
let cal = prompt('cal');
let num2 = +prompt('num2');
switch (cal) {
  case '+':
    alert(`${num1} + ${num2} 的结果是 ${num1 + num2}`)
    break;
  case '-':
    alert(`${num1} - ${num2} 的结果是 ${num1 - num2}`)
    break;
  case '*':
    alert(`${num1} * ${num2} 的结果是 ${num1 * num2}`)
    break;
  case '/':
    alert(`${num1} / ${num2} 的结果是 ${num1 / num2}`)
    break;
}
```

循环语句

```js
let result = prompt('Do you love me?');
    while (result) {
      if (result === 'yes') {
        alert('I love you too');
        break; # break是退出循环,continue是略过循环
      }
    }
```

取款机案例

```js
let result = 0;
    while (true) {
      const doWhat = +prompt(`请输入操作:
      1.存钱
      2.取钱
      3.查看余额
      4.退出`)
      if (doWhat === 4) {
        break
      }
      switch (doWhat) {
        case 1:
          let putIn = +prompt('请输入存款金额');
          result += putIn;
          break;
        case 2:
          let takeOut = +prompt('请输入取款金额');
          if (result < takeOut) {
            alert('您的余额不足')
            break;
          }
          result -= takeOut;
          break;
        case 3:
          alert(`您的余额为${result}`)
          break;
      }
    }
```

### 循环

#### for循环语句

```js
for (起始值; 结束条件; 变量变化量) {
	#循环体
}
```

#### 案例

```js
# 打印1-100岁
for (let age = 1; age <= 100; age++) {
	document.write(`我今年${age}岁了<br>`)
}
# 1-100偶数的和
let sum = 0;
for (let num = 1; num <= 100; num++) {
	if(num % 2 === 0) {
		sum += num
	}
}
document.write(`1-100偶数的和是${sum}`)
# 打印5个五角星
for (let i = 0; i < 5; i++) {
  document.write('☆')
}
# 打印数组
const arr = ['马超', '张飞', '关羽', '黄忠', '赵云'];
for (let i = 0; i < arr.length; i++) {
  document.write(`${arr[i]}<br>`)
}
# 99乘法表
for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= i; j++) {
    let result = i * j;
    if (result < 10) {
      result = '&nbsp&nbsp' + result
    }
    document.write(`<span>${j}×${i}=${result}</span>`)
  }
  document.write('<br>')
}
```

### 数组

Array是一种可以按顺序保存数据的数据类型

- 声明数值

  - `let 数组名 = [值1, 值2, 值3, ......]`
  - `let arr = new Array(1, 2, 3, 4)`

- 取值语法

  - 数组名[下标]

- 遍历数组

  - 语法

    ```js
    for (i = 0, i < 数组名.length, i++) {
    	数组名[i]
    }
    ```

- 案例

  ```js
  for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
          max = arr[i]
        }
        if (arr[i] < min) {
          min = arr[i]
        }
      }
      document.write(`最大值是${max}`)
      document.write(`最小值是${min}`)
  ```

- 操作数组

| 查数组              | 改数组      | 增数组                                                       | 删数组                                                       |
| ------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| console.log(arr[i]) | arr[i] = 10 | arr.push('str') #在后面增加<br />arr.unshift('str') #在前面增加 | arr.pop() #删除最后<br />arr.shift() #删除最开头<br />arr.splice(start, deleteCount) |

数组筛选

```js
let arr = [2, 0, 6, 1, 77, 0, 52, 0, 25, 7];
// 声明新的数组
let newArr = [];
// 遍历旧的数组
for (let i = 0; i < arr.length; i++) {
  if (arr[i] >= 10) {
      // 满足条件 追加给新数组
    newArr.push(arr[i])
  }
}
// 输出新的数组
document.write(newArr)
```

冒泡排序(了解即可)

```js
let arr = [5, 4, 3, 2, 1];
for (let i = 0; i < arr.length - 1; i++) {
  for (let j = 0; j < arr.length - i - 1; j++) {
    if (arr[j] > arr[j + 1]) {
      let tep = arr[j + 1];
      arr[j + 1] = arr[j]
      arr[j] = tep;
    }
  }
}
console.log(arr)
```

实际开发中

`arr.sort()`

### function

使用

```js
//声明函数
function 函数名 () {
    函数体
}
//调用/calling/running/invoking function
函数名()
```

命名规则

- 基本和变量一致
- 驼峰命名法 getNumber
- 最好开头用动词 get\can\has\set

函数参数

```js
function 函数名(参数) {
    函数体
}
//数组求和
const getSum = (arr = []) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }
  console.log(sum)
}
getSum([1, 2, 3, 4, 5])
```

函数的返回值

```js
function fn() {
    return 20 // 返回值
}
let num = fn()
console.log(num)
```

注意事项
- return 终止函数，后面的代码不会被执行
- return 只能返回一个值，是最后的一个
- 多个可以用数组
- 有返回值是return后面的值，没有返回undefined

**案例巩固**

利用函数求数组[151,5800,10,1,7]中的最大值
```js
function getarrMax(arr){
    var max = arr[0];
    for(var i = 1; i <= arr.length; i++){
        if (arr[i]) > max;
        max = arr[i];
    }
    return max;
}
console.log(getarrMax[151,5800,10,1,7]);
```

arguments的使用

```js
function fn(){
    console.log(arguments); # 里面存储了所有传递过来的实参
}
fn(1,2,3,4);
```
arguments是伪数组
1. 具有数组的length属性
2. 按照索性的方式进行存储的
3. 不是真数组 pop() push() 等等
4. 只有函数才有arguments对象，并且内置好了

函数的三种声明方式

1. 利用函数关键字自定义函数(命名函数)
    ```js
    function fn() {
    
    }
    fn();
    ```

2. 函数表达式(匿名函数)
    ```js
    const fn = function () {
    
    }
    fn();
    ```

3. ES6箭头函数

   ```js
   const fn = () => {
       
   }
   fn();
   ```

   

作用域

- 代码名字(变量)在某个范围内起作用和效果;目的为了提高程序的可靠性，减少命名冲突
- js的作用域`es6`之前:全局作用域 局部作用域
- 全局作用域:整个script标签 或者是一个单独的js文件`var num = 10;`
- 局部作用域:在函数内部`function fn(){}`

### 预解析

**重点**

1. js引擎运行分两步:预解析>代码执行
   - 预解析:js引擎会把所有的var和function提升到最前面
   - 代码执行:按照代码代码书写顺序从上往下执行
2. 预解析分为变量提升和函数提升
   - 变量提升:所有变量声明提升到最前面，不提升赋值操作
   - 函数提升:所有函数声明提升到最前面，不调用

