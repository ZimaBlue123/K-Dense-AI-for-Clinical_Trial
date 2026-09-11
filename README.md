# Scientific-Skills-for-Clinical_Trial

涓枃 | [English](README.en.md)

涓村簥璇曢獙 / 涓村簥鐮旂┒ AI 杈呭姪绯荤粺锛堜粨搴撴牳蹇冨唴瀹癸細`skills/`锛夈€?

## 椤圭洰瀹氫綅

鏈粨搴撶淮鎶や竴缁勯潰鍚戜复搴婄爺绌朵笌涓村簥璇曢獙鐨?AI skills/鎶€鑳斤紝瑕嗙洊涓村簥璇曢獙妫€绱€佸惊璇?鍐崇瓥鏀寔銆佷复搴婃姤鍛婁笌鍚堣鏂囨。銆佺粺璁′笌寤烘ā銆佺敓瀛樺垎鏋愩€佸彲瑙ｉ噴鎬э紝浠ュ強甯哥敤鍖诲/绉戠爺鏁版嵁搴撹闂瓑宸ヤ綔娴併€?

## 蹇€熷紑濮?

### 鐜瑕佹眰

- **Python**锛?.10+锛圕I 褰撳墠浣跨敤 3.10锛?
- **AI 瀹㈡埛绔?*锛欳ursor / Claude Code / Codex锛堥渶瑕佹敮鎸?skills 鏈哄埗锛?
- **鍥捐〃娓叉煋锛坄fireworks-tech-graph`锛?*锛歚librsvg`锛堟彁渚?`rsvg-convert` 鍛戒护锛?

`rsvg-convert` 瀹夎绀轰緥锛?

```bash
# macOS
brew install librsvg

# Ubuntu / Debian
sudo apt install librsvg2-bin
```

### 瀹夎锛圥ython 渚濊禆锛?

```bash
python -m pip install -r requirements.txt
```

### 闅愮涓庡悎瑙勶紙寮虹儓寤鸿锛?

- 涓嶈鎶婂師濮嬩釜浣撴暟鎹紙鍚彈璇曡€呭眰闈㈠瓧娈点€佹槑缁嗗鍑猴級鎻愪氦鍒?Git銆傝鎶婅緭鍏?CSV 鏀惧湪 `data/`锛堝凡鍦?`.gitignore` 涓拷鐣ワ級锛屽苟鎶婅緭鍑烘斁鍒?`output/`锛堝悓鏍蜂細琚拷鐣ワ級銆?
- 鎶椾綋鍔ㄥ姏瀛﹀垎鏋愯剼鏈細杈撳嚭鈥滃凡姹囨€?宸插缓妯♀€濈殑缁撴灉锛堝弬鏁般€侀娴嬪潎鍊?CI銆侀槇鍊兼椂闂达級锛屼絾浠嶅缓璁笉瑕佹妸杈撳嚭浜х墿涓婁紶鍒颁笉鍙俊鐜銆?

### 寮€鍙戜笌璐ㄩ噺锛堝彲閫夛級

瀹夎寮€鍙戜緷璧栵紙娴嬭瘯/Lint锛夛細

```bash
python -m pip install -r requirements-dev.txt
```

杩愯娴嬭瘯锛?

```bash
pytest
```

杩愯浠ｇ爜椋庢牸妫€鏌ワ紙鎺ㄨ崘浣跨敤 ruff锛夛細

```bash
ruff check scripts/ tests/
ruff format --check scripts/ tests/
```

> 椤圭洰宸蹭粠 flake8 杩佺Щ鑷?ruff锛堥厤缃 `pyproject.toml`锛夈€俙requirements-dev.txt` 浠嶄繚鐣?flake8 浠ュ吋瀹规棫 CI銆?

娓呯悊鏈湴缂撳瓨/蹇界暐鏂囦欢锛堣皑鎱庝娇鐢紝浼氬垹闄ゆ墍鏈夎 `.gitignore` 蹇界暐鐨勫唴瀹癸級锛?

```bash
git clean -fdX
```

### 瀹夎锛坰kills 鍒板鎴风锛?

濡傛灉浣犵殑瀹㈡埛绔敮鎸?鐩存帴寮曠敤椤圭洰鐩綍"锛屾帹鑽愮洿鎺ユ寚鍚戞湰浠撳簱鐨?`skills/`锛涘惁鍒欏彲澶嶅埗鍒板鎴风鐨勫叏灞€ skills 鐩綍銆?

Windows锛圥owerShell锛夌ず渚嬶細

```powershell
$dst = Join-Path $env:USERPROFILE ".cursor\skills"
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item -Recurse -Force ".\skills\*" $dst

# 浠呭悓姝ュ崟涓?skill锛堢ず渚嬶級
powershell -File .\scripts\sync_skills_to_global.ps1 -Skill pptx-gmc-sync-from-word
```

macOS/Linux锛坆ash锛夌ず渚嬶細

```bash
mkdir -p ~/.cursor/skills
cp -r ./skills/* ~/.cursor/skills/
```

## 浠撳簱缁撴瀯

```
Scientific-Skills-for-Clinical_Trial/
鈹溾攢鈹€ skills/                # 姣忎釜 skill 涓€涓洰褰曪紙鏍稿績鍐呭锛?57 涓級
鈹溾攢鈹€ docs/                  # 闀挎枃妗ｏ紙绱㈠紩瑙佷笅鏂?鏂囨。绱㈠紩"锛?
鈹溾攢鈹€ scripts/               # 浠撳簱绾у彲鎵ц鑴氭湰鍏ュ彛锛堝惈 CSR/瀹℃牳鎶ュ憡鐢熸垚锛?
鈹?  鈹溾攢鈹€ common_scripts/    # 鍏变韩宸ュ叿妯″潡锛堝 docx_utils锛?
鈹?  鈹斺攢鈹€ _archive/          # 宸插綊妗ｇ殑鍘嗗彶鐗堟湰锛堜笉鍐嶇淮鎶わ級
鈹溾攢鈹€ tests/                 # 娴嬭瘯
鈹溾攢鈹€ pyproject.toml         # 椤圭洰鍏冩暟鎹?+ ruff/mypy/pytest 閰嶇疆
鈹溾攢鈹€ requirements.txt
鈹溾攢鈹€ requirements-dev.txt
鈹斺攢鈹€ CONTRIBUTING.md
```

缁存姢绾﹀畾涓庢洿璇︾粏瑙ｉ噴瑙?`docs/repo_layout.md`銆?

---

## 寮€鍙戝伐浣滄祦

鏈粨搴撳湪姣忔閲嶅ぇ閲嶆瀯鏃朵細璺戜竴缁?*鑷鑴氭湰**锛堜綅浜?`scripts/_tools/`锛夈€傝繖浜涜剼鏈彲鐙珛浜?IDE / CI 杩愯锛屾柟渚夸汉宸ユ帓鏌ャ€?

```bash
# Phase 1: py_compile + pyflakes 鍏ㄩ噺鎵弿
py -3 scripts/_tools/_audit_phase1_compile.py
py -3 scripts/_tools/_audit_phase1_pyflakes.py
py -3 scripts/_tools/_audit_phase1_ast.py

# Phase 2: 鎵弿鍐椾綑鏂囦欢 / 涓存椂鏃ュ織锛堜笉鍒犻櫎锛?
py -3 scripts/_tools/_audit_phase2_scan.py
# 鎷熷垹闄ゆ竻鍗曞啓鍏?docs/cleanup_phase2_plan.md

# Phase 3: 瀵煎叆渚濊禆瀹¤锛堜笌 requirements.txt 瀵圭収锛?
py -3 scripts/_tools/_audit_phase3_imports.py
```

鎶ュ憡鍒嗗埆钀藉湪锛?

- `docs/audit_phase1.md` 鈥斺€?闈欐€佸垎鏋?+ AST 娣卞害瀹℃煡
- `docs/cleanup_phase2_plan.md` 鈥斺€?鍒犻櫎娓呭崟锛堝惈椋庨櫓绛夌骇锛?
- `reports/phase3_imports.md` 鈥斺€?绗笁鏂?import 浣跨敤鐭╅樀



---

## Skills 娓呭崟涓庝娇鐢ㄦ柟娉?

鏈粨搴撳寘鍚?**157 涓?skills**锛堝凡鍚堝苟涓婃父 scientific-skills 鐨勯潪閲嶅鏉＄洰锛夛紝鍒嗕负浠ヤ笅鍑犵被锛?

### 鏍稿績鏁版嵁鍒嗘瀽 Skills

| Skill | 鐢ㄩ€?| 蹇€熶娇鐢?|
|-------|------|----------|
| `exploratory-data-analysis` | 200+ 鏍煎紡绉戠爺鏁版嵁 EDA | `python skills/exploratory-data-analysis/scripts/eda_analyzer.py <file>` |
| `statistical-analysis` | 鍋囪妫€楠屻€佹晥搴旈噺銆丄PA 鎶ュ憡 | `from scripts.assumption_checks import comprehensive_assumption_check` |
| `antibody-kinetics` | 鎶椾綋鍔ㄥ姏瀛?鍏嶇柅鎸佷箙鎬э細骞傚緥妯″瀷 + MixedLM锛屾敮鎸?M12+ 澶栨帹涓庨槇鍊兼椂闂?| `python skills/antibody-kinetics/scripts/run_antibody_kinetics_pipeline.py --infile data/subject.csv --outdir output/antibody-kinetics --threshold 10` |
| `scikit-learn` | 缁忓吀 ML 寤烘ā涓庣绾?| `python skills/scikit-learn/scripts/classification_pipeline.py` |
| `scikit-survival` | 鐢熷瓨鍒嗘瀽锛圕ox/RSF/GBS锛?| 瑙?SKILL.md 涓殑浠ｇ爜绀轰緥 |
| `shap` | 妯″瀷鍙В閲婃€э紙SHAP values锛?| `shap.TreeExplainer(model)(X_test)` |

### 楂樻€ц兘鏁版嵁澶勭悊 Skills

| Skill | 鐢ㄩ€?| 蹇€熶娇鐢?|
|-------|------|----------|
| `polars` | 楂樻€ц兘 DataFrame/ETL | 瑙?`references/core_concepts.md` |
| `dask` | 澶ф暟鎹?瓒呭唴瀛樺鐞?| 瑙?`references/dataframes.md` |
| `vaex` | 鍗佷嚎琛岀骇鏁版嵁澶勭悊 | 瑙?`references/core_dataframes.md` |

### 鍖诲鏁版嵁搴撴绱?Skills

| Skill | 鐢ㄩ€?| 蹇€熶娇鐢?|
|-------|------|----------|
| `clinicaltrials-database` | ClinicalTrials.gov API v2 | `python skills/clinicaltrials-database/scripts/query_clinicaltrials.py` |
| `pubmed-database` | PubMed E-utilities 妫€绱?| 瑙?`references/api_reference.md` |
| `openalex-database` | OpenAlex 鏂囩尞妫€绱?| `python skills/openalex-database/scripts/openalex_client.py` |
| `database-lookup` | 鑱氬悎鏁版嵁搴撳叆鍙ｏ紙鑷姩璺敱鍒?ClinicalTrials/PubMed/OpenAlex/FDA/ClinVar/ClinPGx/COSMIC锛?| 瑙?`skills/database-lookup/SKILL.md` |
| `paper-lookup` | 鑱氬悎鏂囩尞鍏ュ彛锛堣嚜鍔ㄨ矾鐢卞埌 PubMed/OpenAlex锛屾寜闇€琛ュ厖璇曢獙妫€绱級 | 瑙?`skills/paper-lookup/SKILL.md` |
| `fda-database` | openFDA 鑽搧/鍣ㄦ/鍙洖 | `python skills/fda-database/scripts/fda_query.py` |
| `clinvar-database` | ClinVar 鍙樺紓鑷寸梾鎬?| 瑙?`references/api_reference.md` |
| `clinpgx-database` | ClinPGx 鍩哄洜-鑽墿鐩镐簰浣滅敤 | `python skills/clinpgx-database/scripts/query_clinpgx.py` |
| `cosmic-database` | COSMIC 鐧岀棁浣撶粏鑳炵獊鍙?| `python skills/cosmic-database/scripts/download_cosmic.py` |

### 涓村簥鏂囨。涓庢姤鍛?Skills

| Skill | 鐢ㄩ€?| 蹇€熶娇鐢?|
|-------|------|----------|
| `clinical-reports` | 鐥呬緥鎶ュ憡/CSR/SAE锛圕ARE/ICH-E3锛?| `python skills/clinical-reports/scripts/validate_case_report.py` |
| `clinical-decision-support` | 闃熷垪鍒嗗眰/寰瘉鎺ㄨ崘锛圠aTeX/PDF锛?| `python skills/clinical-decision-support/scripts/create_cohort_tables.py` |
| `treatment-plans` | 涓綋鍖栨不鐤楄鍒掞紙LaTeX/PDF锛?| `python skills/treatment-plans/scripts/generate_template.py` |

### 宸ュ叿绫?Skills

| Skill | 鐢ㄩ€?| 蹇€熶娇鐢?|
|-------|------|----------|
| `markitdown` | 鏂囦欢杞?Markdown锛圥DF/DOCX/PPTX绛夛級 | `markitdown document.pdf -o output.md` |
| `perplexity-search` | AI 瀹炴椂缃戠粶鎼滅储 | `python skills/perplexity-search/scripts/perplexity_search.py "query"` |
| `github-proxy-push` | GitHub 浠ｇ悊鎺ㄩ€?| 瑙?SKILL.md |
| `pyhealth` | 鍖荤枟 AI锛圗HR 浠诲姟/妯″瀷锛?| 瑙?`references/datasets.md` |
| `csr-stage-docx-workflow` | CSR 闃舵鎬у皬缁?Word 鐢熸垚 | `python scripts/_archive/generate_csr_docx.py` |
| `word-audit-report-format` | Word 瀹℃牳鎶ュ憡瀛椾綋瑙勮寖 | `python scripts/_archive/generate_audit_report_docx.py` |
| `pptx-gmc-sync-from-word` | Word GMC/渚嬫暟/P 鍊煎悓姝ュ埌 PPT 鎸囧畾椤佃〃鏍?| `python skills/pptx-gmc-sync-from-word/scripts/sync_pptx_from_word.py --word <docx> --ppt <pptx>` |
| `docx-to-markdown` | DOCX 鏂囨湰/琛ㄦ牸鎶藉彇涓?Markdown | `python skills/docx-to-markdown/scripts/extract_docx_text.py` |

### 鍥捐〃 Skill锛堥」鐩唴缃級

| Skill | 鐢ㄩ€?| 瀹夎浣嶇疆 | 蹇€熶娇鐢?|
|-------|------|----------|----------|
| `fireworks-tech-graph` | 閫氳繃鑷劧璇█鐢熸垚鎶€鏈浘锛堟灦鏋勫浘/娴佺▼鍥?搴忓垪鍥?UML锛夛紝瀵煎嚭 SVG+PNG | `skills/fireworks-tech-graph` | Prompt 绀轰緥锛歚鐢讳竴涓?RAG 鏋舵瀯鍥撅紝style 2锛岃緭鍑哄埌 ./output/` |

璇存槑锛?
- 璇?skill 鏉ユ簮锛歔`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)銆?
- `fireworks-tech-graph` 宸插苟鍏ユ湰椤圭洰 `skills/` 鐩綍缁熶竴绠＄悊銆?
- 鏇存柊璇?skill锛圵indows/PowerShell锛夛細

```powershell
git -c http.proxy= -c https.proxy= -C ".\skills\fireworks-tech-graph" pull
```

---

## Skill 璇︾粏浣跨敤绀轰緥

### 1. exploratory-data-analysis锛圗DA锛?

**鍦烘櫙**锛氬绉戠爺鏁版嵁鏂囦欢杩涜鑷姩鍖栨帰绱㈠垎鏋?

```bash
# 鍛戒护琛屼娇鐢?
python skills/exploratory-data-analysis/scripts/eda_analyzer.py data.csv output_report.md

# 鏀寔 200+ 鏍煎紡锛欳SV, FASTQ, PDB, HDF5, TIFF, mzML 绛?
```

**Prompt 妯℃澘**锛?
```
璇峰鏂囦欢 <path/to/data> 鍋?EDA锛氳瘑鍒牸寮忋€佸瓧娈?缁村害銆佺己澶?寮傚父銆佽川閲忛棶棰橈紝骞惰緭鍑?markdown 鎶ュ憡涓庝笅涓€姝ュ缓璁€?
```

### 2. statistical-analysis锛堢粺璁″垎鏋愶級

**鍦烘櫙**锛氬亣璁炬楠屻€佹晥搴旈噺璁＄畻銆丄PA 鏍煎紡鎶ュ憡

```python
from scripts.assumption_checks import comprehensive_assumption_check

# 缁煎悎鍋囪妫€楠岋紙鍚彲瑙嗗寲锛?
results = comprehensive_assumption_check(data=df, value_col="score", group_col="group", alpha=0.05)
```

**Prompt 妯℃澘**锛?
```
鎴戞湁鏁版嵁闆?<path/to.csv>锛屼富瑕佺粨灞€=<Y>锛屽垎缁?<group>锛涜甯垜閫夋嫨鍚堥€傛楠屻€佸仛鍋囪妫€鏌ワ紝骞舵寜 APA 椋庢牸杈撳嚭缁撴灉涓庢晥搴旈噺銆?
```

### 3. scikit-survival锛堢敓瀛樺垎鏋愶級

**鍦烘櫙**锛氫复搴婅瘯楠?time-to-event 鍒嗘瀽

```python
from sksurv.util import Surv
from sksurv.ensemble import RandomSurvivalForest
from sksurv.metrics import concordance_index_ipcw

# 鍒涘缓鐢熷瓨缁撳眬
y = Surv.from_dataframe("event", "time", df)

# 璁粌妯″瀷
rsf = RandomSurvivalForest(n_estimators=100, random_state=42)
rsf.fit(X_train, y_train)

# 璇勪及锛圲no's C-index锛屾帹鑽愮敤浜庨珮鍒犲け鏁版嵁锛?
c_uno = concordance_index_ipcw(y_train, y_test, rsf.predict(X_test))[0]
```

**Prompt 妯℃澘**锛?
```
瀵?<path/to.csv> 鍋氱敓瀛樺垎鏋愶細time=<time_col>, event=<event_col>锛涙瘮杈?Cox/RSF/GBS锛屾姤鍛?Uno C-index銆両BS锛屽苟缁欏嚭椋庨櫓鍒嗗眰銆?
```

### 4. clinicaltrials-database锛堜复搴婅瘯楠屾绱級

**鍦烘櫙**锛氭绱?ClinicalTrials.gov 鎷涘嫙涓殑璇曢獙

```python
import requests

url = "https://clinicaltrials.gov/api/v2/studies"
params = {"query.cond": "breast cancer", "filter.overallStatus": "RECRUITING", "pageSize": 10}
response = requests.get(url, params=params)
data = response.json()
print(f"Found {data['totalCount']} trials")
```

**Prompt 妯℃澘**锛?
```
鍦?ClinicalTrials.gov 妫€绱細condition=<鐤剧梾>锛宨ntervention=<鑽墿/鐤楁硶>锛宻tatus=RECRUITING锛屽湴鍖?<鍥藉/宸?锛涜緭鍑哄墠 20 鏉″姣旇〃骞舵€荤粨鍏ユ帓鏍囧噯銆?
```

### 5. shap锛堟ā鍨嬪彲瑙ｉ噴鎬э級

**鍦烘櫙**锛氳В閲婃満鍣ㄥ涔犳ā鍨嬮娴?

```python
import shap

# 鍒涘缓瑙ｉ噴鍣紙鏍戞ā鍨嬬敤 TreeExplainer锛?
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)

# 鍏ㄥ眬閲嶈鎬?
shap.plots.beeswarm(shap_values)

# 鍗曚釜棰勬祴瑙ｉ噴
shap.plots.waterfall(shap_values[0])
```

**Prompt 妯℃澘**锛?
```
璇峰鎴戣缁冨ソ鐨勬ā鍨嬪仛 SHAP 瑙ｉ噴锛歜eeswarm+bar+3 涓釜浣?waterfall锛屽苟鎸囧嚭鍙兘鐨勬暟鎹硠婕忕壒寰併€?
```

### 6. perplexity-search锛圓I 缃戠粶鎼滅储锛?

**鍦烘櫙**锛氳幏鍙栨渶鏂扮鐮斾俊鎭紙瓒呭嚭妯″瀷鐭ヨ瘑鎴鏃ユ湡锛?

```bash
# 璁剧疆 API Key
export OPENROUTER_API_KEY='sk-or-v1-your-key-here'

# 鎼滅储
python skills/perplexity-search/scripts/perplexity_search.py "What are the latest CAR-T therapy clinical trials in 2024?"

# 浣跨敤楂樼骇妯″瀷
python skills/perplexity-search/scripts/perplexity_search.py "query" --model sonar-pro-search
```

### 7. markitdown锛堟枃浠惰浆鎹級

**鍦烘櫙**锛氬皢 PDF/DOCX/PPTX 绛夎浆涓?Markdown

```bash
# 鍛戒护琛?
markitdown document.pdf -o output.md

# Python API
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

---

## 鎺ㄨ崘宸ヤ綔娴?

### 浠庢暟鎹埌璇佹嵁鐨勫畬鏁存祦绋?

```
1) exploratory-data-analysis 鈫?鏁版嵁璐ㄩ噺宸℃
2) statistical-analysis 鈫?鍋囪妫€楠屼笌 APA 鎶ュ憡
3) scikit-learn 鎴?scikit-survival 鈫?寤烘ā
4) shap 鈫?妯″瀷瑙ｉ噴
```

闇€瑕佽ˉ鍏呰瘉鎹?璇曢獙淇℃伅鏃讹細骞惰浣跨敤 `clinicaltrials-database` + `pubmed-database`/`openalex-database`銆?

### 蹇€?Prompt 妯℃澘

```text
璇峰厛瀵?<path/to/data.csv> 鍋?exploratory-data-analysis锛氳瘑鍒瓧娈点€佺己澶便€佸紓甯稿拰璐ㄩ噺闂锛?
鐒跺悗鐢?statistical-analysis 缁欏嚭閫傚綋妫€楠屼笌 APA 椋庢牸鎶ュ憡锛?
鎺ョ潃鐢?scikit-learn 鍋氫竴涓彲澶嶇幇鐨?baseline锛堝惈 CV 涓庢寚鏍囷級锛?
鏈€鍚庣敤 shap 杈撳嚭鍏ㄥ眬涓?3 涓釜浣撳眰闈㈢殑瑙ｉ噴锛屽苟鎻愮ず鍙兘鐨勬暟鎹硠婕忕壒寰併€?
```

---

## 甯哥敤鍏ュ彛

- **Skills 瀵艰锛堟帹鑽愬伐浣滄祦锛?*锛歚docs/skills_guide.md`
- **Skills 娓呭崟涓?prompt 妯℃澘**锛歚docs/skills_catalog.md`
- **璐＄尞鎸囧崡**锛歚CONTRIBUTING.md`

## 鏂囨。绱㈠紩锛坉ocs/锛?

- `docs/skills_guide.md`锛歋kills 瀵艰涓庢帹鑽愬伐浣滄祦锛堢粰浣跨敤鑰咃級
- `docs/skills_catalog.md`锛歋kills 娓呭崟涓庡父鐢?prompt 妯℃澘锛堢粰浣跨敤鑰咃級
- `docs/repo_layout.md`锛氫粨搴撶洰褰曡鑼冧笌缁存姢绾﹀畾锛堢粰缁存姢鑰咃級

## 姣忎釜 skill 鐨勮鏄庡叆鍙?

- **浣跨敤璇存槑**锛氫紭鍏堢湅瀵瑰簲鐩綍鐨?`SKILL.md`
- **鍙傝€冭祫鏂?*锛氱粺涓€鏀惧湪 `references/INDEX.md`锛堝瀛樺湪锛?
- **琛ュ厖鏂囨。锛圧EADME锛?*锛氶儴鍒?skill 鐩綍鎻愪緵棰濆 README锛堣涓嬫柟鐩磋揪閾炬帴锛?
- **椤圭洰瑙勫垯璁板繂**锛氬凡鍦?`.cursor/rules/skills-location-policy.mdc` 鍥哄寲鈥渟kill 浠呮斁椤圭洰 `skills/` 鐩綍鈥?

### Skills 琛ュ厖 README 鐩磋揪閾炬帴

- `skills/fireworks-tech-graph/README.zh.md`锛堜腑鏂囪鏄庯級
- `skills/fireworks-tech-graph/README.md`锛堣嫳鏂囪鏄庯級
- `skills/fireworks-tech-graph/scripts/README.md`锛堣剼鏈鏄庯級

---

## 甯哥敤鑴氭湰

### 鑴氭湰绱㈠紩

| 鑴氭湰 | 鐢ㄩ€?| 鐘舵€?|
|------|------|------|
| `scripts/convert_to_md.py` | 鏂囨。杞琈arkdown锛堟帹鑽愶級 | 鉁?鎺ㄨ崘 |
| `scripts/_archive/md_to_docx.py` | Markdown杞琖ord | 鉁?鎺ㄨ崘 |
| `scripts/_archive/generate_csr_docx.py` | CSR阶段性小结 |
| `scripts/project_self_check.py` | 椤圭洰鑷 | 鉁?鎺ㄨ崘 |
| `scripts/cleanup_generated_artifacts.py` | 娓呯悊缂撳瓨涓嶪DE鍘嗗彶璁板綍 | 鉁?鎺ㄨ崘 |
| `scripts/on_open_cleanup.cmd` | 寮€鏈?鎵撳紑椤圭洰鏃惰嚜鍔ㄦ竻鐞?| 鉁?杈呭姪 |
| `scripts/register_cleanup_logon_task.ps1` | 娉ㄥ唽寮€鏈鸿嚜鍚竻鐞嗕换鍔?| 鉁?杈呭姪 |

### 宸插簾寮冭剼鏈?

> 浠ヤ笅鑴氭湰宸茶搴熷純锛屽姛鑳藉凡鍚堝苟鍒?`convert_to_md.py`锛?

| 鑴氭湰 | 鏇夸唬鏂规 | 璇存槑 |
|------|----------|------|
| `scripts/extract_docx_full.py` | `convert_to_md.py --mode standard` | 鏂囨湰鎻愬彇鍔熻兘宸插悎骞?|
| `scripts/extract_doc_text.py` | `convert_to_md.py` | .doc鏂囨湰鎻愬彇锛圵indows COM锛?|

### 濡備綍閫夋嫨

```
闇€瑕佷粠docx鎻愬彇绾枃鏈紵
  鈫?python scripts/convert_to_md.py input.docx -o output.md

闇€瑕佸甫缂栧彿娈佃惤鎻愬彇锛?#P1, ##T1鏍囪锛夛紵
  鈫?python scripts/convert_to_md.py input.docx -o output.md --mode numbered

闇€瑕佸皢Markdown杞崲涓篧ord锛?
  鈫?python scripts/md_to_docx.py input.md -o output.docx
```

> 浠ヤ笅鑴氭湰閽堝鐗瑰畾浜у搧锛岄€氱敤鍦烘櫙璇蜂娇鐢ㄤ笂鏂规帹鑽愯剼鏈細

| 鑴氭湰 | 鐢ㄩ€?|
|------|------|
| `scripts/_archive/generate_audit_report_docx.py` | 通用审核报告 |
| `scripts/_archive/generate_clinical_doc_audit_report.py` | 临床文档审核报告 |
| `scripts/_archive/generate_clinical_overview_doc_review_docx.py` | 临床概览审核Word |
| `scripts/_archive/generate_phase_summary_doc_review_docx.py` | 阶段总结审核Word |
| `scripts/_archive/generate_norovirus_review_docx.py` | 诺如病毒综述 |
| `scripts/_archive/cansino_detail4843_manual_docx.py` | 康希诺产品专用 |
| `scripts/extract_tables_to_docx.py` | OCR图片转Word表格 |

### 鏂囨。瀹℃牳宸ヤ綔娴侊紙绱犳潗 鈫?Markdown 鈫?Word锛?

#### 1) 灏?DOCX/XLSX/PDF 杞垚 Markdown

```bash
# 鍗曟枃浠?
python scripts/convert_to_md.py input.docx -o output.md

# 鎵归噺鏂囦欢澶癸紙杈撳嚭鍒?review_materials/converted/锛?
python scripts/convert_to_md.py --folder review_materials -o review_materials/converted
```

#### 2) 灏?Markdown 瀹℃牳鎶ュ憡杞垚 Word

```bash
python scripts/md_to_docx.py "review_materials/<浣犵殑瀹℃牳鎶ュ憡>.md" -o "review_materials/<浣犵殑瀹℃牳鎶ュ憡>.docx"
```

#### 3) 鐢熸垚 CSR 闃舵鎬у皬缁擄紙Word锛?

```bash
python scripts/_archive/generate_csr_docx.py --root "椤圭洰鏍圭洰褰?
```

鎻愮ず锛歚review_materials/` 宸插湪 `.gitignore` 涓拷鐣ワ紝涓嶄細琚笂浼犲埌 GitHub銆?

### Word 鏂囨。澶勭悊鎶€宸?

**鏂囦欢鍚嶅惈涓枃鏃?*锛氱洿鎺ュ湪鍛戒护琛屼紶閫掕矾寰勫彲鑳藉洜缂栫爜闂澶辫触锛屽缓璁厛鐢?PowerShell 澶嶅埗涓虹畝鍗曟枃浠跺悕锛?

```powershell
# 澶嶅埗涓虹函鑻辨枃鏂囦欢鍚?
Copy-Item "review_materials\1-3-1璇存槑-20260529-鏂?docx" target.docx

# 鐒跺悗鐢ㄨ剼鏈鐞?
python scripts/convert_to_md.py target.docx -o output.md
```

---

## 鏉ユ簮涓庡綊灞烇紙鍚堣澹版槑锛?

- **涓婃父椤圭洰**锛氭湰浠撳簱浠?[`K-Dense-AI/claude-scientific-skills`](https://github.com/K-Dense-AI/claude-scientific-skills.git) 鎻愬彇骞惰鍓嚭鏇磋仛鐒?涓村簥鐮旂┒/涓村簥璇曢獙"鍦烘櫙鐨勪竴閮ㄥ垎 skills銆?
- **闄勫姞鏉ユ簮**锛歚skills/fireworks-tech-graph` 鏉ヨ嚜 [`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph)锛圡IT License锛夈€?
- **璁稿彲璇?*锛氫笂娓镐笌鏈粨搴撳潎涓?MIT License锛涙湰浠撳簱鍦ㄥ啀鍒嗗彂鏃朵繚鐣欎笂娓哥増鏉冧笌璁稿彲澹版槑锛堝惈鏂板绗笁鏂?skill 鐗堟潈澹版槑锛夈€?
- **鏀瑰姩鑼冨洿锛堟憳瑕侊級**锛氬垹闄や笌涓村簥鐮旂┒鏃犲叧鐨?skills/鏂囨。锛屼粎淇濈暀骞堕噸缁勪笌涓村簥鐮旂┒鐩稿叧鐨?skills锛涜ˉ鍏呮湰浠撳簱鐨勭洰褰曡鑼冦€佷緷璧栦笌 CI銆?
- **闈炶儗涔﹀０鏄?*锛氭湰浠撳簱涓虹ぞ鍖虹淮鎶ょ殑瑁佸壀/鏁寸悊鐗堟湰锛屼笉浠ｈ〃涓婃父浣滆€呮垨缁勭粐鐨勫畼鏂圭珛鍦恒€佽璇佹垨鑳屼功銆?

## 璁稿彲璇?

鏈」鐩噰鐢?MIT 璁稿彲璇侊紝璇﹁ `LICENSE.md`銆?

娉ㄦ剰锛氬悇 skill 鍙兘鏈夌嫭绔嬭鍙瘉鎴栧澶栭儴鏁版嵁婧?SDK 鏈夐澶栭檺鍒讹紝浣跨敤鍓嶈鏌ョ湅瀵瑰簲 skill 鐨?`SKILL.md`銆?
