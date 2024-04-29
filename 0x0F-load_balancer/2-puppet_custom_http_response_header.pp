# Configure Nginx with custom HTTP response header and custom pages in Puppet

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/html':
  ensure => 'directory',
  require => Package['nginx'],
}

file { '/etc/nginx/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => File['/etc/nginx/html'],
}

file { '/etc/nginx/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
  require => File['/etc/nginx/html'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => @(EOF)
    server {
      listen 80;
      listen [::]:80 default_server;
      root   /etc/nginx/html;
      index  index.html index.htm;
      add_header X-Served-By $::hostname;

      location /redirect_me {
        return 301 https://github.com/MedBens02;
      }

      error_page 404 /404.html;
      location /404 {
        root /etc/nginx/html;
        internal;
      }
    }
    | EOF
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  require    => File['/etc/nginx/sites-available/default'],
}

