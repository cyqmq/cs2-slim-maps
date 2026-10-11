#!/usr/bin/env python3
"""将 depot 2347770 中的地图 VPK 打包为预构建 zip（路径前缀 game/csgo/maps/）。

用法: python build_map_zips.py <depot_maps_dir> <output_dir> [map1 map2 ...]
不指定地图时，打包以下 7 个新地图。
"""
import os
import sys
import time
import zipfile

MAPS = ["de_ancient", "de_anubis", "de_cache", "de_nuke",
        "de_overpass", "de_train", "de_vertigo"]


def main():
    depot_maps = sys.argv[1]
    out_dir = sys.argv[2]
    maps = sys.argv[3:] or MAPS
    os.makedirs(out_dir, exist_ok=True)
    for m in maps:
        src = os.path.join(depot_maps, f"{m}.vpk")
        if not os.path.exists(src):
            print(f"WARN: 缺少 {src}，跳过")
            continue
        out = os.path.join(out_dir, f"{m}.zip")
        arc = os.path.join("game", "csgo", "maps", f"{m}.vpk")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            info = zipfile.ZipInfo(arc, time.gmtime(os.path.getmtime(src))[:6])
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, open(src, "rb").read())
        size_mb = os.path.getsize(src) / 1024 / 1024
        print(f"已生成 {out} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()