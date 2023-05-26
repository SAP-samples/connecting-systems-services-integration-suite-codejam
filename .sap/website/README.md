# Generate a static website from content

In case accessing the content through a repo is a bit cumbersome for the reader, it is possible to generate a static website from the content that's available in this repo. To achieve this we can leverage [Jekyll](https://jekyllrb.com/) and [GitHub pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#static-site-generators). 

```bash
# Copy the _config.yml and Gemfile in this directory to the root director
cp _config.yml.sample ../../_config.yml
cp Gemfile.sample ../../Gemfile

# Let's move to the root directory
cd ../../

# Install that's specified in Gemfile
bundle install

# Generate all static content
bundle exec jekyll build

# View the website, it will run on http://localhost:4000
bundle exec jekyll serve
```