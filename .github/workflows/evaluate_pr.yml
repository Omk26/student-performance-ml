name: Evaluate PR Model

on:
  pull_request:
    branches: [main]

permissions:
  contents: write
  pull-requests: write

jobs:
  evaluate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout PR code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install pandas numpy scikit-learn

      - name: Get PR author username
        id: pr_info
        run: |
          echo "author=${{ github.event.pull_request.user.login }}" >> $GITHUB_OUTPUT

      - name: Run evaluation
        id: eval
        run: |
          python evaluate_pr.py --contributor "${{ steps.pr_info.outputs.author }}"

      - name: Commit updated leaderboard
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add leaderboard.csv
          git diff --cached --quiet || git commit -m "📊 Update leaderboard for PR #${{ github.event.pull_request.number }} by ${{ steps.pr_info.outputs.author }}"
          git push origin HEAD:main

      - name: Comment on PR with results
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const csv = fs.readFileSync('leaderboard.csv', 'utf8');
            const lines = csv.trim().split('\n');
            const header = lines[0].split(',');
            
            // Find the latest entry for this contributor
            const contributor = '${{ steps.pr_info.outputs.author }}';
            const entry = lines.slice(1).reverse().find(l => l.includes(contributor));
            
            let resultMsg = '⚠️ Could not find result for this contributor.';
            if (entry) {
              const cols = entry.split(',');
              const model = cols[1];
              const mse = parseFloat(cols[2]).toFixed(4);
              const r2 = parseFloat(cols[3]).toFixed(4);
              resultMsg = `| ${cols[0]} | ${model} | ${mse} | ${r2} |`;
            }

            // Build full leaderboard table
            let table = '| ' + header.join(' | ') + ' |\n';
            table += '|' + header.map(() => '---').join('|') + '|\n';
            lines.slice(1).forEach(line => {
              const cols = line.split(',');
              table += '| ' + cols.join(' | ') + ' |\n';
            });

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## 🎓 Model Evaluation Results\n\n### Your submission:\n| Contributor | Model | MSE | R2 |\n|---|---|---|---|\n${resultMsg}\n\n### 🏆 Full Leaderboard:\n${table}\n\n✅ Leaderboard updated automatically!`
            });
