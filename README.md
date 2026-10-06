# cs2-slim-maps

CS2 Slim 服务端的**地图组件仓库**（选配组件）。
配合主仓库 [cs2-slim-replica](https://github.com/cyqmq/cs2-slim-replica) 使用，按需为精简服务端添加竞技地图。

## 地图列表

| 地图 | 组件目录 | filelist 片段 | 预构建包 |
|------|----------|---------------|----------|
| Dust II | `de_dust2`（核心，主仓库自带） | `game/csgo/maps/de_dust2.vpk` | 无 |
| Mirage | `de_mirage` | `game/csgo/maps/de_mirage.vpk` | [de_mirage.zip](https://github.com/cyqmq/cs2-slim-maps/releases/latest/download/de_mirage.zip) |
| Inferno | `de_inferno` | `game/csgo/maps/de_inferno.vpk` | [de_inferno.zip](https://github.com/cyqmq/cs2-slim-maps/releases/latest/download/de_inferno.zip) |
| Ancient | `de_ancient` | `game/csgo/maps/de_ancient.vpk` | 无 |
| Anubis | `de_anubis` | `game/csgo/maps/de_anubis.vpk` | 无 |
| Cache | `de_cache` | `game/csgo/maps/de_cache.vpk` | 无 |
| Nuke | `de_nuke` | `game/csgo/maps/de_nuke.vpk` | 无 |
| Overpass | `de_overpass` | `game/csgo/maps/de_overpass.vpk` | 无 |
| Train | `de_train` | `game/csgo/maps/de_train.vpk` | 无 |
| Vertigo | `de_vertigo` | `game/csgo/maps/de_vertigo.vpk` | 无 |

## 使用方法

### 方式一：源码构建（推荐，无需 Steam depot 下载）

把需要的竞地图加入 `maps` 列表并写入 `slim.yaml`：

```yaml
platform: win64
maps:
  - de_dust2
  - de_mirage
  - de_inferno
```

然后：

```bash
python cs2slim.py download --config slim.yaml
python cs2slim.py extract  --config slim.yaml
python cs2slim.py build    --config slim.yaml
```

脚本会把本仓库的 `filelist.txt` 片段合并进核心下载清单，一次性下载全部内容。

### 方式二：纯命令行参数

```bash
python cs2slim.py download --platform linux --maps de_dust2,de_mirage --features bots
```

### 方式三：预构建包直接拼装（prebuilt）

从 Release 下载地图 zip 包，**解压到精简树根目录**即可（zip 内已含 `game/csgo/maps/` 路径）：

```bash
# 以 Mirage 为例（slim 或 slim-win 树根目录）
curl -fsSL -o de_mirage.zip https://github.com/cyqmq/cs2-slim-maps/releases/latest/download/de_mirage.zip
unzip -o de_mirage.zip -d <精简树>
```

也可以使用主仓库一键脚本 / CLI 的 prebuilt 模式，自动完成核心包 + 地图包 + 功能包拼装：

```bash
# 一键脚本（Linux，先 export 再 curl|bash）
export CS2_MODE=prebuilt CS2_MAPS=de_dust2,de_mirage
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash

# CLI 等价
python cs2slim.py prebuilt --config slim.yaml
```

预构建包通常为整张地图的 VPK（约 250MB），省去逐文件提取与下载清单解析。

## Release

- **v1.0.0**：`de_mirage.zip`、`de_inferno.zip`（预构建地图包）

## 组件格式

每个地图组件包含：

- `filelist.txt` — 追加到核心 `filelist_2347770.txt` 的片段（通常 = 精确路径）
- `metadata.json` — 元数据（depot、大小、更新时间）

```json
{
  "name": "Mirage",
  "depot": 2347770,
  "required": false,
  "filelist": ["game/csgo/maps/de_mirage.vpk"],
  "size_mb": 250,
  "updated": "2026-10-06"
}
```

## 原理

核心 filelist 已包含全部 prefabs、3dskybox 等，选配地图只需把地图 VPK 追加进下载清单。地图 VPK 自带全部内容（含 bots 导航），无需额外 loose 文件。

## 更新流程

CS2 更新后，检查地图 VPK 路径是否变化，更新 `metadata.json` 的 `updated` 字段即可。