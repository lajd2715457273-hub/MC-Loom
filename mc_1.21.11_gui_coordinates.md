# Minecraft 1.21.11 容器 GUI 反编译坐标参考

> 来源：客户端 JAR（`cache/client_1.21.11.jar`）经 JADX 反编译后的源码  
> 用途：为 `containers.html` 提供与原版完全一致的坐标、尺寸、纹理路径  
> 生成时间：2026-07-30

---

## 1. 基础约定

- 所有坐标均以 **GUI 背景左上角** 为原点 `(0, 0)`。
- 屏幕类继承链：`gti<T extends dhi>`（抽象容器屏幕）→ 各具体屏幕。
- 默认屏幕宽度 `gti.d = 176`。
- 默认屏幕高度 `gti.e = gwv.d`（实测/推断为 `166`）。
- 箱子类特殊：`gtw.e = gtq.a + rows * 18`，其中 `gtq.a = 113`（= 17 上边框 + 96 玩家背包区高度）。
- 槽位尺寸：16×16，槽位间距 18（含 2px 边框/间隙）。
- 玩家背包调用 `c(inventory, 8, startY)` 表示从 `(8, startY)` 开始放置 3 行背包 + 1 行快捷栏。
- 快捷栏位于背包第三行下方 4px 处。

---

## 2. 文件与类对应关系

| 反编译文件 | 对应原版类 | 说明 |
|---|---|---|
| `gti.java` | `AbstractContainerScreen` | 抽象容器屏幕基类 |
| `gtw.java` | `ChestScreen`（generic_54） | 箱子/大箱子屏幕 |
| `dhs.java` | `ChestMenu` | 箱子容器菜单 |
| `guj.java` | `HopperScreen` | 漏斗屏幕 |
| `dik.java` | `HopperMenu` | 漏斗容器菜单 |
| `gug.java` | `FurnaceScreen` | 熔炉屏幕 |
| `gtj.java` | `AbstractFurnaceScreen` | 熔炉/烟熏炉/高炉屏幕基类 |
| `dhk.java` | `AbstractFurnaceMenu` | 熔炉容器菜单 |
| `dih.java` | `FurnaceMenu` | 熔炉具体菜单 |
| `guc.java` | `DispenserScreen` | 发射器/投掷器屏幕 |
| `die.java` | `DispenserMenu` | 发射器/投掷器菜单 |
| `gty.java` | `CraftingScreen` | 工作台屏幕 |
| `dic.java` | `CraftingMenu` | 工作台菜单 |
| `gtn.java` | `AnvilScreen` | 铁砧屏幕 |
| `dhm.java` | `AnvilMenu` | 铁砧菜单 |
| `dhj.java` | `RecipeBookMenu` | 配方书相关菜单基类 |

---

## 3. 各容器详细数据

### 3.1 大箱子 `generic_54`

**源码依据**：`dhs.java`、`gtw.java`

```java
// dhs.java：槽位排列
public dhs(dis<?> $$0, int $$1, ddl $$2, ccv $$3, int $$4) {
    super($$0, $$1);
    a($$3, $$4 * 9);
    this.m = $$3;
    this.n = $$4;          // 行数：大箱子 = 6
    $$3.a((cgd) $$2.j);
    d($$3, 8, 18);          // 箱子槽位从 (8, 18) 开始
    int $$6 = 18 + (this.n * 18) + 13;
    c($$2, 8, $$6);         // 玩家背包从 y = 139 开始
}

private void d(ccv $$0, int $$1, int $$2) {
    for (int $$3 = 0; $$3 < this.n; $$3++) {
        for (int $$4 = 0; $$4 < 9; $$4++) {
            a(new dji($$0, $$4 + ($$3 * 9), $$1 + ($$4 * 18), $$2 + ($$3 * 18)));
        }
    }
}

// gtw.java：背景绘制与尺寸
public gtw(dhs $$0, ddl $$1, yh $$2) {
    super($$0, $$1, $$2);
    this.E = $$0.m();                       // E = 6
    this.e = gtq.a + (this.E * 18);         // 113 + 108 = 221
    this.v = this.e - 94;
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = (this.o - this.d) / 2;
    int $$5 = (this.p - this.e) / 2;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, (this.E * 18) + 17, 256, 256);
    $$0.a(hpa.at, D, $$4, $$5 + (this.E * 18) + 17, 0.0f, 126.0f, this.d, 96, 256, 256);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 纹理 | `textures/gui/container/generic_54.png` |
| 尺寸 | 176 × 221 |
| 箱子槽位起点 | (8, 18) |
| 箱子行数/列数 | 6 行 × 9 列 |
| 玩家背包起点 | (8, 139) |
| 快捷栏起点 | (8, 197) |
| 背景 UV 裁剪 | `[0, 0, 176, 221]` |

---

### 3.2 小箱子 `generic_27`

**源码依据**：`dhs.java`（`n = 3`）、`gtw.java`

```java
// dhs.a(…) 创建 n=1 的单行；dhs.b(…) n=2；dhs.c(…) n=3
public static dhs a(int $$0, ddl $$1) { return new dhs(dis.a, $$0, $$1, 1); }
public static dhs b(int $$0, ddl $$1) { return new dhs(dis.b, $$0, $$1, 2); }
public static dhs c(int $$0, ddl $$1) { return new dhs(dis.c, $$0, $$1, 3); }
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 纹理 | `textures/gui/container/generic_54.png` |
| 尺寸 | 176 × 167（= 3×18 + 113） |
| 箱子槽位起点 | (8, 18) |
| 箱子行数/列数 | 3 行 × 9 列 |
| 玩家背包起点 | (8, 85)（= 18 + 54 + 13） |
| 快捷栏起点 | (8, 143) |
| 背景 UV 裁剪 | `[0, 0, 176, 167]` |

---

### 3.3 漏斗 `hopper`

**源码依据**：`dik.java`、`guj.java`

```java
// dik.java
public dik(int $$0, ddl $$1, ccv $$2) {
    super(dis.q, $$0);
    this.n = $$2;
    a($$2, 5);
    $$2.a((cgd) $$1.j);
    for (int $$3 = 0; $$3 < 5; $$3++) {
        a(new dji($$2, $$3, 44 + ($$3 * 18), 20));   // 槽位 (44 + i*18, 20)
    }
    c($$1, 8, 51);                                     // 玩家背包从 y=51 开始
}

// guj.java
public guj(dik $$0, ddl $$1, yh $$2) {
    super($$0, $$1, $$2);
    this.e = 133;                                      // 高度 133
    this.v = this.e - 94;
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = (this.o - this.d) / 2;
    int $$5 = (this.p - this.e) / 2;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 纹理 | `textures/gui/container/hopper.png` |
| 尺寸 | 176 × 133 |
| 漏斗槽位 | (44, 20), (62, 20), (80, 20), (98, 20), (116, 20) |
| 玩家背包起点 | (8, 51) |
| 快捷栏起点 | (8, 109) |
| 背景 UV 裁剪 | `[0, 0, 176, 133]` |

---

### 3.4 熔炉 `furnace`

**源码依据**：`dhk.java`、`gtj.java`、`gug.java`

```java
// dhk.java：容器槽位
public dhk(dis<?> $$0, drd<? extends dpy> $$1, amt<drb> $$2, dja $$3, int $$4, ddl $$5, ccv $$6, dhv $$7) {
    super($$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7);
    a(new dji($$6, 0, 56, 17));     // 输入槽
    a(new dig(this, $$6, 1, 56, 53)); // 燃料槽
    a(new dii($$5.j, $$6, 2, 116, 35)); // 输出槽
    c($$5, 8, 84);                   // 玩家背包从 y=84 开始
    a($$7);
}

// gtj.java：屏幕渲染
protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, this.D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    if (((dhk) this.w).o()) {
        int $$7 = bgj.d(((dhk) this.w).n() * 13.0f) + 1;
        $$0.a(hpa.at, this.E, 14, 14, 0, 14 - $$7, $$4 + 56, (($$5 + 36) + 14) - $$7, 14, $$7);
    }
    int $$9 = bgj.d(((dhk) this.w).m() * 24.0f);
    $$0.a(hpa.at, this.F, 24, 16, 0, 0, $$4 + 79, $$5 + 34, $$9, 16);
}

// gug.java：纹理路径
private static final amo D = amo.b("container/furnace/lit_progress");
private static final amo E = amo.b("container/furnace/burn_progress");
private static final amo F = amo.b("textures/gui/container/furnace.png");
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/furnace.png` |
| 火焰精灵 | `container/furnace/lit_progress` → `textures/gui/sprites/container/furnace/lit_progress.png` |
| 进度箭头精灵 | `container/furnace/burn_progress` → `textures/gui/sprites/container/furnace/burn_progress.png` |
| 尺寸 | 176 × 166 |
| 输入槽 | (55, 16) |
| 燃料槽 | (55, 52) |
| 输出槽 | (116, 35) |
| 火焰绘制位置 | (56, 36)，尺寸 14×14，从底部向上裁剪 |
| 进度箭头位置 | (79, 34)，尺寸 24×16，从左向右裁剪 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |
| 背景 UV 裁剪 | `[0, 0, 176, 166]` |

**动画说明**：
- 火焰：高度 `litH = 1 ~ 14`，绘制时 `y = 36 + (14 - litH)`，即从下往上填充。
- 箭头：宽度 `burnW = 0 ~ 24`，从左侧开始填充。

---

### 3.5 发射器 / 投掷器 `dispenser`

**源码依据**：`die.java`、`guc.java`

```java
// die.java
public die(int $$0, ddl $$1, ccv $$2) {
    super(dis.g, $$0);
    a($$2, 9);
    this.r = $$2;
    $$2.a((cgd) $$1.j);
    d($$2, 62, 17);       // 3x3 网格从 (62, 17) 开始
    c($$1, 8, 84);        // 玩家背包从 y=84 开始
}

protected void d(ccv $$0, int $$1, int $$2) {
    for (int $$3 = 0; $$3 < 3; $$3++) {
        for (int $$4 = 0; $$4 < 3; $$4++) {
            int $$5 = $$4 + ($$3 * 3);
            a(new dji($$0, $$5, $$1 + ($$4 * 18), $$2 + ($$3 * 18)));
        }
    }
}

// guc.java
private static final amo D = amo.b("textures/gui/container/dispenser.png");
protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = (this.o - this.d) / 2;
    int $$5 = (this.p - this.e) / 2;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 纹理 | `textures/gui/container/dispenser.png` |
| 尺寸 | 176 × 166 |
| 3×3 网格起点 | (62, 17) |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |
| 背景 UV 裁剪 | `[0, 0, 176, 166]` |

---

### 3.6 工作台 `crafting_table`

**源码依据**：`dic.java`、`gty.java`

```java
// dic.java
public dic(int $$0, ddl $$1, dhw $$2) {
    super(dis.m, $$0, 3, 3);
    this.y = $$2;
    this.z = $$1.j;
    a(this.z, 124, 35);   // 输出槽 (124, 35)
    d(30, 17);            // 3x3 合成网格从 (30, 17) 开始
    c($$1, 8, 84);        // 玩家背包从 y=84 开始
}

// gty.java
private static final amo D = amo.b("textures/gui/container/crafting_table.png");

protected gpl I() {
    return new gpl(this.z + 5, (this.p / 2) - 49);   // 配方书按钮相对 GUI 位置 (5, 34)
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = (this.p - this.e) / 2;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 纹理 | `textures/gui/container/crafting_table.png` |
| 尺寸 | 176 × 166 |
| 合成网格 3×3 起点 | (30, 17) |
| 输出槽 | (124, 35) |
| 配方书按钮 | (5, 34)，尺寸约 20×18 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |
| 背景 UV 裁剪 | `[0, 0, 176, 166]` |

---

### 3.7 铁砧 `anvil`

**源码依据**：`dhm.java`、`gtn.java`

```java
// dhm.java：槽位与容器逻辑
public dhm(int $$0, ddl $$1, dhw $$2) {
    super(dis.i, $$0, $$1, $$2, o());
    this.y = did.a();
    this.z = false;
    a(this.y);
}

private static dio o() {
    return dio.a()
        .a(0, 27, 47, $$0 -> true)   // 输入槽 1：(27, 47)
        .a(1, 76, 47, $$02 -> true)  // 输入槽 2：(76, 47)
        .a(2, J, 47)                  // 输出槽：(134, 47)，J = 134
        .a();
}

// gtn.java：屏幕渲染与命名输入框
private static final amo D = amo.b("container/anvil/text_field");
private static final amo E = amo.b("container/anvil/text_field_disabled");
private static final amo F = amo.b("container/anvil/error");
private static final amo G = amo.b("textures/gui/container/anvil.png");

protected void I() {
    int $$0 = (this.o - this.d) / 2;
    int $$1 = (this.p - this.e) / 2;
    this.I = new gjn(this.q, $$0 + 62, $$1 + 24, aem.s, 12, yh.c("container.repair"));
    // EditBox：相对 GUI 左上角 (62, 24)，宽度 aem.s（约 103），高度 12
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    super.a($$0, $$1, $$2, $$3);
    $$0.a(hpa.at, ((dhm) this.w).b(0).h() ? D : E, this.z + 59, this.A + 20, 110, 16);
    // 文本框背景精灵：相对位置 (59, 20)，尺寸 110×16
}

protected void e(gir $$0, int $$1, int $$2) {
    if ((((dhm) this.w).b(0).h() || ((dhm) this.w).b(1).h()) && !((dhm) this.w).b(((dhm) this.w).n()).h()) {
        $$0.a(hpa.at, F, $$1 + 99, $$2 + 45, 28, 21);
        // 错误图标：相对位置 (99, 45)，尺寸 28×21
    }
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/anvil.png` |
| 文本框精灵 | `container/anvil/text_field` / `container/anvil/text_field_disabled` → `textures/gui/sprites/container/anvil/text_field.png` |
| 错误图标精灵 | `container/anvil/error` → `textures/gui/sprites/container/anvil/error.png` |
| 尺寸 | 176 × 166 |
| 输入槽 1 | (27, 47) |
| 输入槽 2 | (76, 47) |
| 输出槽 | (134, 47) |
| 文本框背景精灵 | (59, 20)，尺寸 110×16 |
| 命名输入框（EditBox） | (62, 24)，宽度约 103，高度 12 |
| 错误图标 | (99, 45)，尺寸 28×21 |
| 经验等级文字 | y = 67，右对齐 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |
| 背景 UV 裁剪 | `[0, 0, 176, 166]` |

---

### 3.8 高炉 `blast_furnace`

**源码依据**：`dhp.java`、`gtp.java`（继承 `gtj.java`）

```java
// gtp.java
private static final amo D = amo.b("container/blast_furnace/lit_progress");
private static final amo E = amo.b("container/blast_furnace/burn_progress");
private static final amo F = amo.b("textures/gui/container/blast_furnace.png");
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/blast_furnace.png` |
| 火焰精灵 | `container/blast_furnace/lit_progress` |
| 进度箭头精灵 | `container/blast_furnace/burn_progress` |
| 尺寸 | 176 × 166 |
| 输入槽 | (55, 16) |
| 燃料槽 | (55, 52) |
| 输出槽 | (116, 35) |
| 火焰位置 | (56, 36)，尺寸 14×14，底部向上裁剪 |
| 进度箭头位置 | (79, 34)，尺寸 24×16，左侧向右裁剪 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.9 烟熏炉 `smoker`

**源码依据**：`djm.java`、`guy.java`（继承 `gtj.java`）

```java
// guy.java
private static final amo D = amo.b("container/smoker/lit_progress");
private static final amo E = amo.b("container/smoker/burn_progress");
private static final amo F = amo.b("textures/gui/container/smoker.png");
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/smoker.png` |
| 火焰精灵 | `container/smoker/lit_progress` |
| 进度箭头精灵 | `container/smoker/burn_progress` |
| 尺寸 | 176 × 166 |
| 输入槽 | (55, 16) |
| 燃料槽 | (55, 52) |
| 输出槽 | (116, 35) |
| 火焰位置 | (56, 36)，尺寸 14×14 |
| 进度箭头位置 | (79, 34)，尺寸 24×16 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.10 木桶 `barrel`

**源码依据**：无独立 Screen/Menu 类，复用 `dhs.java`/`gtw.java`，`n = 3`

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/barrel.png`（1.21 JAR 中缺失，网页使用 `generic_54.png` 兜底） |
| 尺寸 | 176 × 167 |
| 箱子槽位起点 | (8, 18) |
| 行数/列数 | 3 行 × 9 列 |
| 玩家背包起点 | (8, 85) |
| 快捷栏起点 | (8, 143) |

---

### 3.11 末影箱 `ender_chest`

**源码依据**：无独立 Screen/Menu 类，复用 `dhs.java`/`gtw.java`，`n = 3`

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/generic_54.png`（实际使用箱子通用背景） |
| 尺寸 | 176 × 167 |
| 箱子槽位起点 | (8, 18) |
| 行数/列数 | 3 行 × 9 列 |
| 玩家背包起点 | (8, 85) |
| 快捷栏起点 | (8, 143) |

---

### 3.12 潜影盒 `shulker_box`

**源码依据**：`djf.java`、`guv.java`

```java
// guv.java
private static final amo D = amo.b("textures/gui/container/shulker_box.png");
public guv(djf $$0, ddl $$1, yh $$2) {
    super($$0, $$1, $$2);
    this.e++;          // 高度比 generic_27 多 1
    this.v = this.e - 94;
}
```

```java
// djf.java
public djf(int $$0, ddl $$1, ccv $$2) {
    super(dis.r, $$0);
    a($$2, 27);
    this.n = $$2;
    $$2.a((cgd) $$1.j);
    d($$2, 8, 18);          // 27 槽从 (8, 18) 开始，3 行
    c($$1, 8, 84);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/shulker_box.png` |
| 尺寸 | 176 × 168 |
| 箱子槽位起点 | (8, 18) |
| 行数/列数 | 3 行 × 9 列 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.13 砂轮 `grindstone`

**源码依据**：`dij.java`、`guh.java`

```java
// dij.java
public dij(int $$0, ddl $$1, ccv $$2, ccv $$3) {
    super(dis.j, $$0);
    a($$2, 2);
    this.n = $$2;
    this.o = $$3;
    a(new dji($$2, 0, 49, 19));   // 输入 1
    a(new dji($$2, 1, 49, 40));   // 输入 2
    a(new dii($$1.j, $$3, 2, 129, 34)); // 输出
    c($$1, 8, 84);
}

// guh.java
private static final amo D = amo.b("container/anvil/error");
private static final amo E = amo.b("textures/gui/container/grindstone.png");

protected void e(gir $$0, int $$1, int $$2) {
    if ((((dij) this.w).b(0).h() || ((dij) this.w).b(1).h()) && !((dij) this.w).b(((dij) this.w).n()).h()) {
        $$0.a(hpa.at, D, $$1 + 92, $$2 + 31, 28, 21);
    }
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/grindstone.png` |
| 错误图标精灵 | `container/anvil/error` |
| 尺寸 | 176 × 166 |
| 输入槽 1 | (49, 19) |
| 输入槽 2 | (49, 40) |
| 输出槽 | (129, 34) |
| 错误图标 | (92, 31)，尺寸 28×21 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.14 酿造台 `brewing_stand`

**源码依据**：`dhq.java`、`gtt.java`

```java
// dhq.java
public dhq(int $$0, ddl $$1, ccv $$2, dcf $$3, dhv $$4) {
    super(dis.h, $$0);
    a(new c($$2, 0, 56, 51));          // 药水槽 0
    a(new c($$2, 1, 79, 58));          // 药水槽 1（中下方）
    a(new c($$2, 2, aem.r, 51));       // 药水槽 2（右侧），aem.r = 102
    this.z = new dcf(20);
    a(new dji($$2, 3, 17, 17));        // 烈焰粉燃料槽
    a(new dji(this.z, 4, 79, 17));     // 原料槽
    c($$1, 8, 84);
}

// gtt.java
private static final amo D = amo.b("container/brewing_stand/bubbles");
private static final amo E = amo.b("container/brewing_stand/fuel");
private static final amo C = amo.b("textures/gui/container/brewing_stand.png");

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, C, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    int $$7 = ((dhq) this.w).j();
    int $$8 = bgj.d((28.0f * $$7) / 400.0f);
    if ($$8 > 0) {
        // 气泡：尺寸 12×29，从底部向上裁剪
        $$0.a(hpa.at, D, 12, 29, 0, 29 - $$8, $$4 + 63, ($$5 + 37) + 29 - $$8, 12, $$8);
    }
    int $$10 = ((dhq) this.w).l();
    if ($$10 > 0) {
        // 燃料条：尺寸 18×4，从左向右裁剪
        int $$11 = bgj.d((18.0f * $$10) / 20.0f);
        $$0.a(hpa.at, E, 18, 4, 0, 0, $$4 + 60, $$5 + 44, $$11, 4);
    }
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/brewing_stand.png` |
| 气泡精灵 | `container/brewing_stand/bubbles` |
| 燃料精灵 | `container/brewing_stand/fuel_length`（JAR 中实际文件名为 `fuel_length.png`） |
| 尺寸 | 176 × 166 |
| 药水槽 0（左） | (56, 51) |
| 药水槽 1（中下） | (79, 58) |
| 药水槽 2（右） | (102, 51) |
| 烈焰粉燃料槽 | (17, 17) |
| 原料槽 | (79, 17) |
| 气泡动画位置 | (63, 37)，尺寸 12×29，底部向上裁剪 |
| 燃料条位置 | (60, 44)，尺寸 18×4，左侧向右裁剪 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.15 附魔台 `enchanting_table`

**源码依据**：`dif.java`、`guf.java`

```java
// dif.java
public dif(int $$0, ddl $$1, ccv $$2, ddq $$3, dhv $$4) {
    super(dis.e, $$0);
    this.r = $$3;
    a(this.r);
    a(new dji($$2, 0, 15, 47));        // 待附魔物品槽
    a(new dji(this.r, 1, 35, 47));     // 青金石槽
    c($$1, 8, 84);
}

// guf.java
private static final amo D = amo.b("textures/gui/container/enchanting_table.png");

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    // 绘制书：以 (34, 47) 为中心旋转
    // 三个附魔选项按钮在 (60, 14), (60, 33), (60, 52)，每个 108×19
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/enchanting_table.png` |
| 青金石槽精灵 | `container/slot/lapis_lazuli` |
| 尺寸 | 176 × 166 |
| 待附魔物品槽 | (15, 47) |
| 青金石槽 | (35, 47) |
| 附魔选项 1 | (60, 14)，尺寸 108×19 |
| 附魔选项 2 | (60, 33)，尺寸 108×19 |
| 附魔选项 3 | (60, 52)，尺寸 108×19 |
| 书的动画区域 | 中心 (34, 47) |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.16 织布机 `loom`

**源码依据**：`diq.java`、`gup.java`

```java
// diq.java
public diq(int $$0, ddl $$1, ccv $$2, ccv $$3, ccv $$4) {
    super(dis.n, $$0);
    a(new dji($$2, 0, 13, 26));       // 旗帜槽
    a(new dji($$3, 1, 33, 26));       // 染料槽
    a(new dji($$4, 2, 23, 45));       // 图案槽
    a(new dii($$1.j, $$1.j, 3, 143, 57)); // 输出槽
    c($$1, 8, 84);
}

// gup.java
private static final amo D = amo.b("textures/gui/container/loom.png");
private static final amo E = amo.b("container/loom/banner_slot");
private static final amo F = amo.b("container/loom/pattern");
private static final amo G = amo.b("container/loom/pattern_highlighted");
private static final amo H = amo.b("container/loom/pattern_selected");
private static final amo I = amo.b("container/loom/scroller");
private static final amo J = amo.b("container/loom/scroller_disabled");

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    // 图案列表 4×4，每个 14×14，起点 (60, 13)
    // 滚动条 (119, 13)，轨道高度 56
    // 输出预览 (141, 8)，尺寸 20×40
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/loom.png` |
| 输出预览精灵 | `container/loom/banner_slot` |
| 图案精灵 | `container/loom/pattern` |
| 图案高亮精灵 | `container/loom/pattern_highlighted` |
| 图案选中精灵 | `container/loom/pattern_selected` |
| 滚动条精灵 | `container/loom/scroller` / `scroller_disabled` |
| 尺寸 | 176 × 166 |
| 旗帜槽 | (13, 26) |
| 染料槽 | (33, 26) |
| 图案槽 | (23, 45) |
| 输出槽 | (143, 57) |
| 图案网格起点 | (60, 13) |
| 图案单元格 | 4 列 × 4 行，每格 14×14 |
| 滚动条 | (119, 13)，尺寸 12×15，轨道高度 56 |
| 输出预览 | (141, 8)，尺寸 20×40 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.17 制图台 `cartography_table`

**源码依据**：`dhr.java`、`gtu.java`

```java
// dhr.java
public dhr(int $$0, ddl $$1, ccv $$2, ccv $$3) {
    super(dis.f, $$0);
    this.n = $$2;
    this.o = $$3;
    a(new dji($$2, 0, 15, 15));        // 地图槽
    a(new dji($$3, 1, 15, 52));        // 纸槽
    a(new dii($$1.j, $$1.j, 2, 145, 39)); // 输出槽
    c($$1, 8, 84);
}

// gtu.java
private static final amo D = amo.b("textures/gui/container/cartography_table.png");
private static final amo E = amo.b("container/cartography_table/scaled_map");
private static final amo F = amo.b("container/cartography_table/map_overlay");
private static final amo G = amo.b("container/cartography_table/locked");

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    // 输出地图预览 (67, 13)，尺寸 66×66
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/cartography_table.png` |
| 缩放地图精灵 | `container/cartography_table/scaled_map` |
| 地图覆盖精灵 | `container/cartography_table/map_overlay` |
| 锁定图标精灵 | `container/cartography_table/locked` |
| 尺寸 | 176 × 166 |
| 地图槽 | (15, 15) |
| 纸槽 | (15, 52) |
| 输出槽 | (145, 39) |
| 输出地图预览 | (67, 13)，尺寸 66×66 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.18 锻造台 `smithing_table`

**源码依据**：`djl.java`、`gux.java`

```java
// djl.java
public djl(int $$0, ddl $$1, ccv $$2, ccv $$3, ccv $$4, ccv $$5) {
    super(dis.o, $$0);
    this.n = $$2;
    this.o = $$3;
    this.p = $$4;
    this.q = $$5;
    a(new dji($$2, 0, 8, 48));     // 模板槽
    a(new dji($$3, 1, 26, 48));    // 装备/基础槽
    a(new dji($$4, 2, 44, 48));    // 材料槽
    a(new dii($$1.j, $$5, 3, 98, 48)); // 输出槽
    c($$1, 8, 84);
}

// gux.java
private static final amo D = amo.b("container/anvil/error");
private static final amo E = amo.b("textures/gui/container/smithing.png");

protected void e(gir $$0, int $$1, int $$2) {
    if ((((djl) this.w).b(0).h() || ((djl) this.w).b(1).h() || ((djl) this.w).b(2).h()) && !((djl) this.w).b(((djl) this.w).n()).h()) {
        $$0.a(hpa.at, D, $$1 + 65, $$2 + 46, 28, 21);
    }
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/smithing.png` |
| 错误图标精灵 | `container/anvil/error` |
| 尺寸 | 176 × 166 |
| 模板槽 | (8, 48) |
| 装备/基础槽 | (26, 48) |
| 材料槽 | (44, 48) |
| 输出槽 | (98, 48) |
| 错误图标 | (65, 46)，尺寸 28×21 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.19 切石机 `stonecutter`

**源码依据**：`djo.java`、`guz.java`

```java
// djo.java
public djo(int $$0, ddl $$1, ccv $$2, dqs $$3) {
    super(dis.p, $$0);
    this.n = $$3;
    a(new dji($$2, 0, 20, 33));        // 输入槽
    a(new dii($$1.j, $$1.j, 1, 143, 33)); // 输出槽
    c($$1, 8, 84);
}

// guz.java
private static final amo D = amo.b("textures/gui/container/stonecutter.png");
private static final amo E = amo.b("container/stonecutter/recipe_highlighted");
private static final amo F = amo.b("container/stonecutter/recipe_selected");

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    // 配方列表 4 列 × 3 行，起点 (52, 14)，单元格 16×18
    // 滚动条 (119, 15)，轨道高度 54，尺寸 12×15
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/stonecutter.png` |
| 配方高亮精灵 | `container/stonecutter/recipe_highlighted` |
| 配方选中精灵 | `container/stonecutter/recipe_selected` |
| 尺寸 | 176 × 166 |
| 输入槽 | (20, 33) |
| 输出槽 | (143, 33) |
| 配方列表起点 | (52, 14) |
| 配方单元格 | 4 列 × 3 行，每格 16×18 |
| 滚动条 | (119, 15)，尺寸 12×15，轨道高度 54 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.20 信标 `beacon`

**源码依据**：`dho.java`、`gto.java`

```java
// dho.java
public dho(int $$0, ddl $$1, ccv $$2, dcd $$3, dqj $$4) {
    super(dis.k, $$0);
    this.q = $$3;
    this.r = $$4;
    a(this.q);
    a(new dji($$2, 0, 136, 110));   // 贡品槽
    c($$1, 36, 137);                 // 玩家背包从 (36, 137) 开始
}

// gto.java
private static final amo D = amo.b("textures/gui/container/beacon.png");
private static final amo E = amo.b("container/beacon/payment_slot");
private static final amo F = amo.b("container/beacon/check");
private static final amo G = amo.b("container/beacon/selected_effect");
private static final amo H = amo.b("container/beacon/effect_background");
private static final amo I = amo.b("container/beacon/effect_highlight");
private static final amo J = amo.b("container/beacon/confirm");

public gto(dho $$0, ddl $$1, yh $$2) {
    super($$0, $$1, $$2);
    this.d = 230;    // 宽 230
    this.e = 219;    // 高 219
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = this.A;
    $$0.a(hpa.at, D, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
    int $$7 = ((dho) this.w).m();
    // 确认按钮 (this.d/2 - 45, 219 - 25)，尺寸 90×22
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/beacon.png` |
| 贡品槽精灵 | `container/beacon/payment_slot` |
| 确认按钮精灵 | `container/beacon/confirm` |
| 效果背景精灵 | `container/beacon/effect_background` |
| 效果高亮精灵 | `container/beacon/effect_highlight` |
| 已选效果精灵 | `container/beacon/selected_effect` |
| 对勾精灵 | `container/beacon/check` |
| 尺寸 | 230 × 219 |
| 贡品槽 | (136, 110) |
| 确认按钮 | (70, 194)，尺寸 90×22 |
| 主效果按钮区 | (36, 24) 起始 |
| 次效果按钮区 | (36, 72) 起始 |
| 玩家背包起点 | (36, 137) |
| 快捷栏起点 | (36, 195) |

---

### 3.21 马 `horse`

**源码依据**：`dil.java`、`guk.java`

```java
// dil.java
public dil(int $$0, ddl $$1, ccv $$2, ccv $$3, ccv $$4) {
    super(dis.l, $$0);
    a(new dji($$2, 0, 8, 18));    // 鞍槽
    a(new dji($$3, 1, 8, 36));    // 盔甲槽
    this.n = $$4;
    if (this.n != null) {
        for (int $$6 = 0; $$6 < $$7; $$6++) {
            for (int $$7 = 0; $$7 < 5; $$7++) {
                // 箱子槽位，3 行 × 5 列，起点 (80, 18)
                a(new dji($$4, 2 + ($$7 + ($$6 * 5)), 80 + ($$7 * 18), 18 + ($$6 * 18)));
            }
        }
    }
    c($$1, 8, 84);
}

// guk.java
private static final amo D = amo.b("textures/gui/container/horse.png");
```

**关键数据**（无箱子版本）：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/horse.png` |
| 尺寸 | 176 × 166 |
| 鞍槽 | (8, 18) |
| 盔甲槽 | (8, 36) |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

**有箱子版本**：

| 项目 | 值 |
|---|---|
| 尺寸 | 176 × 166（或更高，视箱子行数而定） |
| 箱子槽位起点 | (80, 18) |
| 箱子槽位布局 | 3 行 × 5 列 |

---

### 3.22 玩家背包 `inventory`

**源码依据**：`dim.java`、`gul.java`

```java
// dim.java
public dim(ddl $$0) {
    super(null, 0, 2, 2);   // 2x2 合成网格
    this.m = $$0;
    d(98, 18);               // 合成槽从 (98, 18) 开始
    a(new dji($$0, 0, 8, 8));   // 头盔
    a(new dji($$0, 1, 8, 26));  // 胸甲
    a(new dji($$0, 2, 8, 44));  // 护腿
    a(new dji($$0, 3, 8, 62));  // 靴子
    a(new dji($$0, 40, 77, 62)); // 副手槽
    c($$0, 8, 84);
}

// gul.java
private static final amo a = amo.b("textures/gui/container/inventory.png");

protected gpl I() {
    return new gpl(this.z + aem.t, (this.p / 2) - 22);
    // 配方书按钮：相对 GUI 左上角 (aem.t, 61)，aem.t ≈ 141
}

protected void a(gir $$0, float $$1, int $$2, int $$3) {
    int $$4 = this.z;
    int $$5 = (this.p - this.e) / 2;
    $$0.a(hpa.at, a, $$4, $$5, 0.0f, 0.0f, this.d, this.e, 256, 256);
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/inventory.png` |
| 尺寸 | 176 × 166 |
| 2×2 合成槽 | (98, 18), (116, 18), (98, 36), (116, 36) |
| 合成输出槽 | (154, 28) |
| 头盔槽 | (8, 8) |
| 胸甲槽 | (8, 26) |
| 护腿槽 | (8, 44) |
| 靴子槽 | (8, 62) |
| 副手槽 | (77, 62) |
| 配方书按钮 | (141, 61) 左右，尺寸 20×18 |
| 玩家背包起点 | (8, 84) |
| 快捷栏起点 | (8, 142) |

---

### 3.23 村民交易 `merchant` / `villager`

**源码依据**：`diu.java`、`gur.java`

```java
// diu.java
public diu(int $$0, ddl $$1, bly $$2) {
    super(dis.s, $$0);
    this.n = $$2;
    a(new dji($$2, 0, 136, 37));   // 交易输入 1
    a(new dji($$2, 1, 162, 37));   // 交易输入 2
    a(new dii($$1.j, $$2, 2, 220, 37)); // 交易输出
    c($$1, 108, 84);                // 玩家背包从 (108, 84) 开始
}

// gur.java
private static final amo D = amo.b("textures/gui/container/villager.png");

public gur(diu $$0, ddl $$1, yh $$2) {
    super($$0, $$1, $$2);
    this.d = 276;    // 宽 276
    this.e = 166;    // 高 166
}
```

**关键数据**：

| 项目 | 值 |
|---|---|
| 背景纹理 | `textures/gui/container/villager.png` |
| 尺寸 | 276 × 166 |
| 交易输入槽 1 | (136, 37) |
| 交易输入槽 2 | (162, 37) |
| 交易输出槽 | (220, 37) |
| 交易列表 | 左侧，y ≈ 17，每项约 20px 高 |
| 玩家背包起点 | (108, 84) |
| 快捷栏起点 | (108, 142) |

---

## 4. 玩家背包通用布局

所有非箱子容器通过 `c(inventory, 8, startY)` 添加玩家背包：

| 容器 | 背包起点 | 快捷栏起点 |
|---|---|---|
| 漏斗 | (8, 51) | (8, 109) |
| 熔炉 / 高炉 / 烟熏炉 | (8, 84) | (8, 142) |
| 发射器 / 投掷器 | (8, 84) | (8, 142) |
| 工作台 | (8, 84) | (8, 142) |
| 铁砧 | (8, 84) | (8, 142) |
| 砂轮 | (8, 84) | (8, 142) |
| 酿造台 | (8, 84) | (8, 142) |
| 附魔台 | (8, 84) | (8, 142) |
| 织布机 | (8, 84) | (8, 142) |
| 制图台 | (8, 84) | (8, 142) |
| 锻造台 | (8, 84) | (8, 142) |
| 切石机 | (8, 84) | (8, 142) |
| 马 | (8, 84) | (8, 142) |
| 玩家背包 | (8, 84) | (8, 142) |

箱子类通过 `dhs.java` 中的 `c($$2, 8, $$6)` 添加，其中 `$$6 = 18 + rows*18 + 13`：

| 类型 | 行数 | 背包起点 | 快捷栏起点 |
|---|---|---|---|
| generic_27 / barrel / ender_chest | 3 | (8, 85) | (8, 143) |
| shulker_box | 3 | (8, 84) | (8, 142) |
| generic_54 | 6 | (8, 139) | (8, 197) |

特殊宽度/偏移容器：

| 容器 | 宽度 | 背包起点 | 快捷栏起点 |
|---|---|---|---|
| 信标 | 230 | (36, 137) | (36, 195) |
| 村民交易 | 276 | (108, 84) | (108, 142) |

---

## 5. 纹理路径映射

Java 源码中使用 `amo.b("...")` 定义 `ResourceLocation`：

- 以 `textures/gui/container/xxx.png` 开头的为旧式整张贴图。
- 以 `container/xxx`、`recipe_book/xxx` 开头的为 1.20.2+ 的 sprite 贴图，对应资源包路径：
  - `assets/minecraft/textures/gui/sprites/<路径>.png`

网页代码中使用的纹理路径（去掉 `.png` 后缀）：

| 用途 | 网页路径 |
|---|---|
| 大/小箱子 / 末影箱背景 | `/gui/container/generic_54` |
| 木桶背景 | `/gui/container/barrel` |
| 潜影盒背景 | `/gui/container/shulker_box` |
| 漏斗背景 | `/gui/container/hopper` |
| 熔炉背景 | `/gui/container/furnace` |
| 熔炉火焰 | `/gui/sprites/container/furnace/lit_progress` |
| 熔炉箭头 | `/gui/sprites/container/furnace/burn_progress` |
| 高炉背景 | `/gui/container/blast_furnace` |
| 高炉火焰 | `/gui/sprites/container/blast_furnace/lit_progress` |
| 高炉箭头 | `/gui/sprites/container/blast_furnace/burn_progress` |
| 烟熏炉背景 | `/gui/container/smoker` |
| 烟熏炉火焰 | `/gui/sprites/container/smoker/lit_progress` |
| 烟熏炉箭头 | `/gui/sprites/container/smoker/burn_progress` |
| 发射器背景 | `/gui/container/dispenser` |
| 工作台背景 | `/gui/container/crafting_table` |
| 配方书按钮 | `/gui/sprites/recipe_book/button` |
| 配方书高亮按钮 | `/gui/sprites/recipe_book/button_highlighted` |
| 铁砧背景 | `/gui/container/anvil` |
| 铁砧文本框 | `/gui/sprites/container/anvil/text_field` |
| 铁砧错误图标 | `/gui/sprites/container/anvil/error` |
| 砂轮背景 | `/gui/container/grindstone` |
| 酿造台背景 | `/gui/container/brewing_stand` |
| 酿造台气泡 | `/gui/sprites/container/brewing_stand/bubbles` |
| 酿造台燃料 | `/gui/sprites/container/brewing_stand/fuel` |
| 附魔台背景 | `/gui/container/enchanting_table` |
| 青金石槽图标 | `/gui/sprites/container/slot/lapis_lazuli` |
| 织布机背景 | `/gui/container/loom` |
| 织布机图案 | `/gui/sprites/container/loom/pattern` |
| 织布机图案高亮 | `/gui/sprites/container/loom/pattern_highlighted` |
| 织布机图案选中 | `/gui/sprites/container/loom/pattern_selected` |
| 织布机滚动条 | `/gui/sprites/container/loom/scroller` |
| 织布机输出预览 | `/gui/sprites/container/loom/banner_slot` |
| 制图台背景 | `/gui/container/cartography_table` |
| 制图台地图 | `/gui/sprites/container/cartography_table/scaled_map` |
| 制图台覆盖 | `/gui/sprites/container/cartography_table/map_overlay` |
| 锻造台背景 | `/gui/container/smithing` |
| 切石机背景 | `/gui/container/stonecutter` |
| 切石机配方高亮 | `/gui/sprites/container/stonecutter/recipe_highlighted` |
| 切石机配方选中 | `/gui/sprites/container/stonecutter/recipe_selected` |
| 信标背景 | `/gui/container/beacon` |
| 信标贡品槽 | `/gui/sprites/container/beacon/payment_slot` |
| 信标确认按钮 | `/gui/sprites/container/beacon/confirm` |
| 信标效果背景 | `/gui/sprites/container/beacon/effect_background` |
| 信标效果高亮 | `/gui/sprites/container/beacon/effect_highlight` |
| 信标已选效果 | `/gui/sprites/container/beacon/selected_effect` |
| 信标对勾 | `/gui/sprites/container/beacon/check` |
| 马背景 | `/gui/container/horse` |
| 玩家背包背景 | `/gui/container/inventory` |
| 村民交易背景 | `/gui/container/villager` |

---

## 6. 已知常量推断

| 常量 | 值 | 来源 |
|---|---|---|
| `gti.d`（默认屏幕宽） | 176 | `gti.java` 第 54 行 |
| `gti.e`（默认屏幕高） | `gwv.d` ≈ 166 | `gti.java` 第 55 行 |
| `gtq.a`（箱子上下两部分之和） | 113 | `gtw.java`：`e = gtq.a + rows*18`，且渲染拆分为 `(rows*18+17)` + `96` |
| 槽位尺寸 | 16×16 | `gti.java` 中物品渲染逻辑 |
| 槽位间距 | 18 | 多处 `col*18`、`row*18` |
| 背包与快捷栏间距 | 4 | `c(...)` 方法标准布局 |
| `aem.r` | 102 | 酿造台第三个药水槽 x 坐标 |
| `aem.s` | 103 | 铁砧命名框宽度 |
| `aem.t` | ≈ 141 | 玩家背包配方书按钮 x 坐标 |

---

## 7. 备注

- 本文件基于 JADX 反编译结果整理，类名/字段名为混淆名（如 `gti`、`dhs`、`gtn` 等）。
- 已完成反编译的容器：大/小箱子、漏斗、熔炉、高炉、烟熏炉、木桶、末影箱、潜影盒、发射器、工作台、铁砧、砂轮、酿造台、附魔台、织布机、制图台、锻造台、切石机、信标、马、玩家背包、村民交易。
- 坐标均经过 `tools/verify_all_containers.py` Playwright 截图验证（验证时同步更新脚本中的类型列表）。
- 若后续新增容器（如收纳袋、命令方块矿车等），应继续反编译对应 `Screen` 与 `Menu` 类并按此格式补充。
