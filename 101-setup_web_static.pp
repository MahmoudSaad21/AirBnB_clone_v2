#!/usr/bin/env bash
# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure data directory exists
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Ensure web_static directory structure is set up
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Ensure fake HTML file is created
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>\n',
  owner   => 'root',
  group   => 'root',
}

# Ensure symbolic link is created
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'root',
  group  => 'root',
}
