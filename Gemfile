# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "jekyll", "~> 4.4"
gem "jekyll-last-modified-at", git: "https://github.com/maximevaillancourt/jekyll-last-modified-at", branch: "add-support-for-files-in-git-submodules"
gem "webrick", "~> 1.9"
gem "nokogiri"


group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

gem "jekyll-sitemap", "~> 1.3"
gem "jekyll-seo-tag", "~> 2.6"
gem "kramdown-parser-gfm", "~> 1.1.0"
gem 'jekyll-loading-lazy', "~> 0.1.1"


gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]