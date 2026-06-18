# 太阳系交互系统 (Solar System Interactive)

基于 **Three.js (WebGL)** 的 3D 太阳系模拟，支持纹理贴图、行星公转/自转、视角交互、点击查看天体介绍。

## 功能
- 太阳 + 八大行星（水星至海王星）
- 土星环、月球绕地球
- 鼠标拖拽旋转视角，滚轮缩放（带边界限制）
- 点击任意天体弹出介绍面板
- 星空背景（银河纹理）
- 所有纹理使用 Base64 内嵌，双击 `index.html` 即可运行

## 运行方式
1. 直接双击 `index.html` 打开（推荐使用 Chrome/Edge）
2. 或使用本地服务器：
   ```bash
   python -m http.server 8000
   # 浏览器访问 http://localhost:8000