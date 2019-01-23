# Route Configuration

This repository is a lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program with Ryu SDN framework to build a simple software-defined network and compare the different between two forwarding rules.

---
## Objectives

1. Learn how to build a simple software-defined networking with Ryu SDN framework
2. Learn how to add forwarding rule into each OpenFlow switch

---
## Overview

1. We will give you a Python code (`SimpleTopo.py`) that includes an example network topology and another Python code (`SimpleController.py`) that includes Ryu controller
2. We will get you a figure illustrating a topology you should generate
3. Copy the necessary function code from `SimpleTopo.py` and `SimpleController.py` to your Python code (`topo.py` and `controller.py`) to build your networks with forwarding rules

---
## Tasks

> **NOTICE:** Please follow this [slides](Tasks.pdf) for detail.

1. Environment Setup
2. Example of Ryu SDN
3. Mininet Topology
4. Ryu Controller
5. Measurement
6. Report

### File Structure

```bash
Route_Configuration/            # This is ./ in this repository
|--- src/                       # Folder of source code
    |--- scripts/               # Folder of scripts
        |--- run_mininet.sh     # Running script of Mininet
        |--- run_ryu.sh         # Running script of Ryu manager
    |--- topo/                  # Folder of topology figure
        |--- topo.png
    |--- out/                   # Output files
        |--- .gitkeep           # For keeping this folder
    |--- SimpleTopo.py          # Example code of topology
    |--- SimpleController.py    # Example code of controller
    |--- controller.py          # Your program should be here!
    |--- topo.py                # Your program should be here!
|--- LICENSE
|--- README.md
|--- .gitignore                 # For ignoring useless files
```

---
## References

* **Ryu SDN**
    * [Ryubook Documentation](https://osrg.github.io/ryu-book/en/html/)
    * [Ryubook [PDF]](https://osrg.github.io/ryu-book/en/Ryubook.pdf)
    * [Ryu 4.30 Documentation](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Ryu Controller Tutorial](http://sdnhub.org/tutorials/ryu/)
    * [OpenFlow 1.3 Switch Specification](https://www.opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf)
    * [Ryubook 說明文件](https://osrg.github.io/ryu-book/zh_tw/html/)
    * [GitHub - Ryu Controller 教學專案](https://github.com/OSE-Lab/Learning-SDN/blob/master/Controller/Ryu/README.md)
    * [Ryu SDN 指南 – Pengfei Ni](https://feisky.gitbooks.io/sdn/sdn/ryu.html)
    * [OpenFlow 通訊協定](https://osrg.github.io/ryu-book/zh_tw/html/openflow_protocol.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributor

* [David Lu](https://github.com/yungshenglu)

---
## License

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)