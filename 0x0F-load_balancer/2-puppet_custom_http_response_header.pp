# Configure Nginx with custom HTTP response header and custom pages in Puppet

# Ensure the package list is always updated before attempting installation
exec { 'update-system':
  command     => '/usr/bin/apt-get update',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
  unless      => "apt-cache policy | grep 'nginx'",
  before      => Package['nginx'],
}

# Install Nginx
package { 'nginx':
  ensure  => installed,
  require => Exec['update-system'],
}

# Configure the main site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled to start at boot
service { 'nginx':
  ensure => running,
  enable => true,
}

# Template for /etc/nginx/sites-available/default
file {'nginx/default.erb':
  path    => "/etc/puppet/modules/nginx/templates/default.erb",
  content => @(EOF)
    server {
      listen 80;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm;

      add_header X-Served-By $::hostname;

      location /redirect_me {
        rewrite ^/redirect_me https://github.com/MedBens02 permanent;
      }

      error_page 404 /404.html;
      location = /404.html {
        root /var/www/html;
        internal;
      }
    }
    | EOF
}
