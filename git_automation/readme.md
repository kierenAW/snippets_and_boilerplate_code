# Git Push Pull

The script <i>pull_all.sh</i> loops through all sub-directories and performs a <i>git pull</i> for each sub-directory. <i>push_all.sh</i> does the same and also performs a <i>git push</i>

<i>reset_pull_all.sh runs <i>git checkout -- *</i> then a <i>git pull</i> this has the effect of removing local changed and pulling from the remote. <b>Take care when using this as you could destroy your own work!</b>


# .gitignore Common Features

### Ignore jupyter checkpoints
\*.ipynb_checkpoints\*

### Ignore datafiles
\*.csv<br>\*.xls<br>\*.xlsx

### Ignore images
\*.png<br>\*.jpg<br>\*.jpeg

# git lfs common files to add
<br> git lfs track "*.pdf"
<br> git lfs track "*.jpg"
<br> git lfs track "*.png"
<br> git lfs track "*.jpeg"
<br> git lfs track "*.tiff"
<br> git lfs track "*.psd"
<br> git lfs track "*.zip"

* Note: be aware of if you want to add these files to types to ignore or git lfs

# Useful Tools
[BFG Repo-Cleaner]("https://rtyley.github.io/bfg-repo-cleaner/") "Removes large or troublesome blobs like git-filter-branch does, but faster. And written in Scala"
