# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "buggybase"
  config.vm.network "private_network",
    ip: "192.168.33.10"

  # Need to install vagrant-docker-compose.
  # Execute commands as follows:
  # $ vagrant plugin install vagrant-docker-compose
  config.vm.provision :docker_compose,
    compose_version: "1.26.0"
  config.vm.provision :docker

  config.vm.synced_folder ".", "/buggybase",
    mount_options: ["ro"]

  config.vm.provision :shell, :inline => <<-EOS
    apt-get update
    apt-get -y upgrade
    cd /buggybase
    docker-compose up -d --build
  EOS
end
