# Minecraft 容器 GUI 分类汇总

> 基于 `containers.html` 当前已实现的 23 种容器整理  
> 生成时间：2026-07-30

---

## 一、按布局结构分类

### 1. 箱子类（Chest-like）

| 容器 | 尺寸 | 行数 | 背包起点 | 备注 |
|---|---|---|---|---|
| 大箱子 `generic_54` | 176×221 | 6 行 × 9 列 | (8, 139) | 标准双箱 |
| 小箱子 `generic_27` | 176×167 | 3 行 × 9 列 | (8, 85) | 与木桶/末影箱共用背景逻辑 |
| 木桶 `barrel` | 176×167 | 3 行 × 9 列 | (8, 85) | 1.21 无独立 GUI 背景，使用 `generic_54.png` 兜底 |
| 末影箱 `ender_chest` | 176×167 | 3 行 × 9 列 | (8, 85) | 使用 `generic_54.png` |
| 潜影盒 `shulker_box` | 176×168 | 3 行 × 9 列 | (8, 84) | 独立背景 `shulker_box.png` |

**共同特征**：槽位按行优先排列，玩家背包位于容器槽位下方 13px 处。

---

### 2. 熔炼类（Furnace-like）

| 容器 | 输入槽 | 燃料槽 | 输出槽 | 动画元素 |
|---|---|---|---|---|
| 熔炉 `furnace` | (55,16) | (55,52) | (116,35) | 火焰 + 冶炼箭头 |
| 高炉 `blast_furnace` | (55,16) | (55,52) | (116,35) | 同熔炉，纹理不同 |
| 烟熏炉 `smoker` | (55,16) | (55,52) | (116,35) | 同熔炉，纹理不同 |

**共同特征**：三槽位呈“品”字形，火焰从底部向上消耗，箭头从左向右填充。

---

### 3. 3×3 网格类

| 容器 | 网格起点 | 输出槽 | 备注 |
|---|---|---|---|
| 发射器 / 投掷器 `dispenser` | (62,17) | 无 | 9 格输入 |
| 工作台 `crafting_table` | (30,17) | (124,35) | 配方书按钮 (5,34) |

---

### 4. 输入-输出类（2-4 个功能槽）

| 容器 | 槽位布局 | 额外交互 |
|---|---|---|
| 漏斗 `hopper` | 1 行 5 槽 (44,20) | 无 |
| 铁砧 `anvil` | (27,47), (76,47), (134,47) | 命名输入框 |
| 砂轮 `grindstone` | (49,19), (49,40), (129,34) | 错误图标 |
| 酿造台 `brewing_stand` | 3 药水 + 烈焰粉 + 原料 | 气泡 + 燃料条动画 |
| 制图台 `cartography_table` | (15,15), (15,52), (145,39) | 输出地图预览 |
| 锻造台 `smithing_table` | (8,48), (26,48), (44,48), (98,48) | 错误图标 |
| 切石机 `stonecutter` | (20,33), (143,33) | 配方网格 + 滚动条 |

---

### 5. 列表/选择类

| 容器 | 列表区域 | 选择交互 |
|---|---|---|
| 织布机 `loom` | 图案网格 4×4 (60,13) | 点击图案切换高亮 |
| 切石机 `stonecutter` | 配方网格 4×3 (52,14) | 点击配方切换高亮 |
| 村民交易 `merchant` | 左侧交易列表 (5,17) | 点击交易项 |
| 信标 `beacon` | 主/次效果按钮 | 点击选择效果 + 确认按钮 |

---

### 6. 特殊界面

| 容器 | 尺寸 | 特殊结构 |
|---|---|---|
| 附魔台 `enchanting_table` | 176×166 | 3 个附魔选项按钮 + 书动画区域 |
| 信标 `beacon` | 230×219 | 贡品槽 + 效果按钮 + 玩家背包偏移 (36,137) |
| 马 `horse` | 176×166 | 鞍槽 (8,18) + 盔甲槽 (8,36) |
| 玩家背包 `inventory` | 176×166 | 2×2 合成 + 盔甲 + 副手 + 配方书按钮 |
| 村民交易 `merchant` | 276×166 | 宽屏布局，交易列表 + 三槽位 |

---

## 二、按交互复杂度分类

### Level 1：纯静态展示

- 大箱子、小箱子、木桶、末影箱、潜影盒
- 漏斗
- 发射器 / 投掷器
- 马

### Level 2：简单点击/切换

- 工作台：配方书按钮切换高亮
- 铁砧：命名输入框可输入
- 砂轮：错误图标显示
- 锻造台：错误图标显示
- 制图台：地图预览

### Level 3：动画效果

- 熔炉、高炉、烟熏炉：火焰 + 箭头动画
- 酿造台：气泡 + 燃料条动画
- 附魔台：书动画区域（当前用静态背景 + 可点击选项模拟）

### Level 4：列表/网格选择

- 织布机：图案网格选择
- 切石机：配方网格选择
- 村民交易：交易列表选择
- 信标：主/次效果按钮 + 确认

---

## 三、按纹理类型分类

### 使用旧式整张贴图（`textures/gui/container/*.png`）

- `generic_54`：大/小箱子、木桶、末影箱
- `shulker_box`：潜影盒
- `hopper`：漏斗
- `furnace` / `blast_furnace` / `smoker`：熔炼类
- `dispenser`：发射器
- `crafting_table`：工作台
- `anvil`：铁砧
- `grindstone`：砂轮
- `brewing_stand`：酿造台
- `enchanting_table`：附魔台
- `loom`：织布机
- `cartography_table`：制图台
- `smithing`：锻造台
- `stonecutter`：切石机
- `beacon`：信标
- `horse`：马
- `inventory`：玩家背包
- `villager`：村民交易

### 使用 1.20.2+ Sprite 贴图

| 容器 | Sprite 元素 |
|---|---|
| 熔炉类 | `container/furnace/lit_progress`、`container/furnace/burn_progress` 等 |
| 铁砧 | `container/anvil/text_field`、`container/anvil/error` |
| 砂轮 | `container/anvil/error` |
| 锻造台 | `container/anvil/error` |
| 酿造台 | `container/brewing_stand/bubbles`、`container/brewing_stand/fuel_length` |
| 附魔台 | `container/slot/lapis_lazuli` |
| 织布机 | `container/loom/pattern`、`pattern_highlighted`、`pattern_selected`、`scroller` |
| 制图台 | `container/cartography_table/scaled_map`、`map` |
| 切石机 | `container/stonecutter/recipe_highlighted`、`recipe_selected` |
| 信标 | `container/beacon/confirm`、`effect_background`、`selected_effect`、`effect_highlight`、`check`、`payment_slot` |
| 工作台/背包 | `recipe_book/button`、`recipe_book/button_highlighted` |

---

## 四、已知纹理兜底与缺失

| 容器/元素 | 实际情况 | 网页处理方式 |
|---|---|---|
| 木桶背景 | 1.21 JAR 中无 `barrel.png` | 使用 `generic_54.png` 兜底 |
| 酿造台燃料条 | JAR 中实际文件为 `fuel_length.png` | 使用 `fuel_length` 路径 |
| 织布机输出预览 | 无 `banner_slot.png` | 使用 `pattern` 替代（可选，失败不影响主渲染） |
| 制图台覆盖层 | 无 `map_overlay.png` | 使用 `map` 替代（可选） |

---

## 五、截图验证清单

已通过 `tools/verify_all_containers.py` 生成截图：

```
screenshots/check_render_generic_54.png
screenshots/check_render_generic_27.png
screenshots/check_render_barrel.png
screenshots/check_render_ender_chest.png
screenshots/check_render_shulker_box.png
screenshots/check_render_furnace.png
screenshots/check_render_blast_furnace.png
screenshots/check_render_smoker.png
screenshots/check_render_hopper.png
screenshots/check_render_dispenser.png
screenshots/check_render_crafting_table.png
screenshots/check_render_anvil.png
screenshots/check_render_grindstone.png
screenshots/check_render_brewing_stand.png
screenshots/check_render_enchanting_table.png
screenshots/check_render_loom.png
screenshots/check_render_cartography_table.png
screenshots/check_render_smithing_table.png
screenshots/check_render_stonecutter.png
screenshots/check_render_beacon.png
screenshots/check_render_horse.png
screenshots/check_render_inventory.png
screenshots/check_render_merchant.png
```

---

## 六、后续可补充

- 驴/骡箱子版本（ horse 容器 chested 变体）
- 收纳袋（bundle）界面
- 命令方块矿车、投掷器等更冷门界面
- 加入鼠标悬停槽位高亮、物品提示框
