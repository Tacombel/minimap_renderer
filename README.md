## Minimap Renderer

![Tests](https://github.com/WoWs-Builder-Team/minimap_renderer/actions/workflows/tests.yml/badge.svg)

Minimap Renderer parses World of Warships replays to create a timelapse video that resembles the in-game minimap.

![enter image description here](images/minimap.gif)

Try it on in [Google Colab](https://colab.research.google.com/drive/1OyomQe5pHaDDozpt0rs9JMg54No8QMjE?usp=sharing)

### Fork Information

This is a fork of the original [WoWs-Builder-Team/minimap_renderer](https://github.com/WoWs-Builder-Team/minimap_renderer), maintained through [In-dor/minimap_renderer](https://github.com/In-dor/minimap_renderer). This fork maintains full compatibility with the **GNU Affero General Public License v3.0 (AGPLv3)** and is provided as a maintained version for production use.

### Installation

1. Install Python 3.10
2. Create a Python virtual environment and activate it.
   - Linux
     ```
     python3.10 -m venv venv && . venv/bin/activate
     ```
   - Windows
     ```
     py -3.10 -m venv venv && venv\Scripts\activate.bat
     ```
   - You should now see `(venv)` at the start of the command prompt.
3. Install the renderer package. To install the renderer package use this command.
   ```
   pip install --upgrade --force-reinstall git+https://github.com/Tacombel/minimap_renderer.git
   ```
   
   Alternatively, you can install from the upstream fork:
   ```
   pip install --upgrade --force-reinstall git+https://github.com/In-dor/minimap_renderer.git
   ```
4. You're all set.

### Usage

Replays can be rendered with `render` module. The full usage is:

```
python -m render --replay <replay_path>
```

This will create a `.mp4` file from your replay file.

Since the renderer is installed to a virtual environment, you need to activate it once before you render. Once activated, you can render any replay file as long as it is a valid replay file.

### License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**. As a derivative work, this fork maintains full compliance with the AGPLv3 license terms, including the requirement to publish any modifications under the same license.

**Attribution Chain:**
- **Original:** [WoWs-Builder-Team/minimap_renderer](https://github.com/WoWs-Builder-Team/minimap_renderer) - AGPLv3
- **Upstream Fork:** [In-dor/minimap_renderer](https://github.com/In-dor/minimap_renderer) - AGPLv3
- **This Fork:** [Tacombel/minimap_renderer](https://github.com/Tacombel/minimap_renderer) - AGPLv3

### Credits and Links

<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" alt="JetBrains Logo (Main) logo." height="200">

- This project is supported by [Jetbrains](https://www.jetbrains.com/) through their [Open Source Support](https://jb.gg/OpenSourceSupport) program.

- This project is maintained by `@notyourfather#7816` and `@Trackpad#1234`.

- However, it would not have been possible without Monstrofil's [replays_unpack](https://github.com/Monstrofil/replays_unpack)!

- A minimal Discord bot wrapper is available [here](https://github.com/WoWs-Builder-Team/minimap_renderer_bot).

- One with additional features is available [here](https://github.com/padtrack/track).
