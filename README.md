# K-Dense-AI-for-Clinical_Trial

临床试验AI辅助系统 - 基于Claude Scientific Skills的临床研究工具集

## 📋 项目简介

本项目整合了[Claude Scientific Skills](claude-scientific-skills-local/)，为临床试验研究提供AI驱动的分析和决策支持工具。通过148+科学技能和250+数据库访问能力，帮助研究人员加速临床试验设计、数据分析和报告生成。

## 🎯 核心功能

- **临床试验设计与分析** - 基于ClinicalTrials.gov数据库的试验检索和分析
- **临床决策支持** - 患者队列分析、治疗推荐、结果预测
- **临床报告生成** - 符合监管要求的病例报告、试验报告、不良事件报告
- **变异解读** - ClinVar、COSMIC、ClinPGx数据库整合的基因变异临床意义分析
- **药物基因组学** - 个体化用药指导和药物相互作用分析
- **多组学整合** - RNA-seq、蛋白质组、代谢组数据的系统生物学分析

## 📦 项目结构

```
K-Dense-AI-for-Clinical_Trial/
├── README.md                          # 本文件
├── claude-scientific-skills-local/    # Claude科学技能库
│   ├── README.md                      # 技能库详细文档
│   ├── docs/                          # 文档和示例
│   └── scientific-skills/             # 148+科学技能
│       ├── clinical-decision-support/ # 临床决策支持
│       ├── clinical-reports/          # 临床报告生成
│       ├── clinvar-database/          # ClinVar变异数据库
│       ├── clinpgx-database/          # 药物基因组学数据库
│       ├── cosmic-database/           # 癌症体细胞突变数据库
│       └── ...                        # 其他科学技能
└── downloads/                         # 下载文件目录
```

## 🚀 快速开始

### 环境要求

- **Python**: 3.9+ (推荐3.12+)
- **uv**: Python包管理器
- **AI客户端**: Cursor、Claude Code或Codex
- **系统**: Windows 10/11、macOS或Linux

### 安装步骤

1. **克隆项目**
```bash
git clone <repository-url>
cd K-Dense-AI-for-Clinical_Trial
```

2. **安装uv包管理器**
```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. **配置技能库**

将技能复制到AI客户端的技能目录：

```bash
# Cursor (全局安装)
cp -r claude-scientific-skills-local/scientific-skills/* ~/.cursor/skills/

# Claude Code (全局安装)
cp -r claude-scientific-skills-local/scientific-skills/* ~/.claude/skills/
```

4. **开始使用**

在AI客户端中直接提问，系统会自动调用相关技能。

## 💡 使用示例

### 临床变异解读

```
使用可用技能分析VCF文件，注释变异的临床意义。查询ClinVar获取致病性评级，
检查COSMIC癌症突变数据库，从NCBI Gene获取基因信息，通过UniProt分析蛋白质影响，
搜索PubMed相关病例报告，查询ClinPGx药物基因组学数据，生成临床报告，
并在ClinicalTrials.gov查找匹配的临床试验。
```

### 临床试验检索与分析

```
使用可用技能在ClinicalTrials.gov搜索肺癌EGFR抑制剂的临床试验，
分析入组标准和排除标准，评估试验设计质量，提取主要终点和次要终点，
生成试验对比报告。
```

### 药物基因组学分析

```
使用可用技能查询ClinPGx数据库，分析患者基因型对华法林代谢的影响，
提供个体化剂量推荐，检查药物相互作用，生成用药指导报告。
```

## 📚 详细文档

完整的技能文档和使用指南请参见：

- **[Claude Scientific Skills完整文档](claude-scientific-skills-local/README.md)** - 148+技能详细说明
- **[使用示例](claude-scientific-skills-local/docs/examples.md)** - 跨领域工作流示例
- **[技能列表](claude-scientific-skills-local/docs/scientific-skills.md)** - 所有可用技能清单

### 临床相关技能

- **[临床决策支持](claude-scientific-skills-local/scientific-skills/clinical-decision-support/)** - 证据综合、结果分析、队列分析
- **[临床报告](claude-scientific-skills-local/scientific-skills/clinical-reports/)** - 病例报告、试验报告、监管合规
- **[ClinVar数据库](claude-scientific-skills-local/scientific-skills/clinvar-database/)** - 变异临床意义注释
- **[ClinPGx数据库](claude-scientific-skills-local/scientific-skills/clinpgx-database/)** - 药物基因组学指导
- **[COSMIC数据库](claude-scientific-skills-local/scientific-skills/cosmic-database/)** - 癌症体细胞突变

## 🤝 贡献

欢迎贡献新的临床试验相关功能和技能！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交Pull Request

## 📄 许可证

本项目采用MIT许可证。详见[LICENSE](LICENSE)文件。

**注意**: 各个技能模块可能有独立的许可证，使用前请查看对应技能的`SKILL.md`文件中的`license`字段。

## 💬 支持与社区

- **问题反馈**: [GitHub Issues](https://github.com/K-Dense-AI/claude-scientific-skills/issues)
- **社区讨论**: [K-Dense Slack社区](https://join.slack.com/t/k-densecommunity/shared_invite/zt-3iajtyls1-EwmkwIZk0g_o74311Tkf5g)
- **企业支持**: [K-Dense官网](https://k-dense.ai/)

## 🌟 致谢

本项目基于[Claude Scientific Skills](https://github.com/K-Dense-AI/claude-scientific-skills)构建，感谢K-Dense团队和开源社区的贡献。

---

**Copyright © 2026** | 基于Claude Scientific Skills构建
