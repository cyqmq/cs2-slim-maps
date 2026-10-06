# cs2-slim-maps

CS2 Slim 服务端的**地图组件仓库**（选配组件）。

配合主仓库 [cs2-slim-replica](https://github.com/cyqmq/cs2-slim-replica) 使用，按需为精简服务端添加竞技地图。

## 地图列表

| 地图 | 组件目录 | filelist 片段 | 预构建包 |
|------|----------|---------------|----------|
| Dust II | `de_dust2`（核心，主仓库必含） | `game/csgo/maps/de_dust2.vpk` | — |
| Mirage | `de_mirage` | `game/csgo/maps/de_mirage.vpk` | 可选 |
| Inferno | `de_inferno` | `game/csgo/maps/de_inferno.vpk` | 可选 |
| Ancient | `de_ancient` | `game/csgo/maps/de_ancient.vpk` | — |
| Anubis | `de_anubis` | `game/csgo/maps/de_anubis.vpk` | — |
| Cache | `de_cache` | `game/csgo/maps/de_cache.vpk` | — |
| Nuke | `de_nuke` | `game/csgo/maps/de_nuke.vpk` | — |
| Overpass | `de_overpass` | `game/csgo/maps/de_overpass.vpk` | — |
| Train | `de_train` | `game/csgo/maps/de_train.vpk` | — |
| Vertigo | `de_vertigo` | `game/csgo/maps/de_vertigo.vpk` | — |

## 使用方法

### 方式一：源码构建（推荐，从 Steam depot 下载）

在主仓库的配置里把地图加入 `maps` 列表，例如 `slim.yaml`：

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

主脚本会把本仓库的 `filelist.txt` 片段合并进核心下载清单，一次下载全部内容。

### 方式二：命令行参数

```bash
python cs2slim.py download --platform linux --maps de_dust2,de_mirage --features bots
```

### 方式三：预构建包（待发布）

从 Release 下载地图包 zip，解压到精简树的 `game/csgo/maps/` 即可。预构建包体积较大（每张图约 250MB VPK），按需发布。

## 组件格式

每个地图组件包含：

- `filelist.txt` — 追加到核心 `filelist_2347770.txt` 的片段（普通行=精确路径）
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

核心 filelist 已包含全部 prefabs（3dskybox 等），选配地图只需把地图 VPK 追加到下载清单。地图 VPK 自包含导航网格（bots 可用），无需额外 loose 文件。

## 更新流程

CS2 更新后，检查地图 VPK 路径是否有变化，更新 `metadata.json` 的 `updated` 字段即可。