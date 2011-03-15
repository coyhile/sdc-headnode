{
    "platform-release": "develop"
  , "build-tgz": "true"
  , "agents-shar": "develop"
  , "datasets": [
      { "name": "smartos-1.3.8"
      , "uri": "https://guest:GrojhykMid@assets.joyent.us/templates/sdc/smartos-1.3.8.zfs.bz2"
      }
    , { "name": "nodejs-0.4.0"
      , "uri": "https://guest:GrojhykMid@assets.joyent.us/datasets/nodejs-0.4.0.zfs.bz2"
      , "needs_extra_node_service_magic": "true"
      }
  ]
  , "adminui-checkout": "origin/develop"
  , "assets-checkout": "origin/develop"
  , "atropos-tarball": "^atropos-develop-.*.tar.bz2$"
  , "ca-tarball": "^ca-pkg-master-.*.tar.bz2$"
  , "capi-checkout": "origin/develop"
  , "dhcpd-checkout": "origin/develop"
  , "mapi-checkout": "origin/develop"
  , "portal-checkout": "origin/develop"
  , "pubapi-checkout": "origin/develop"
  , "rabbitmq-checkout": "origin/develop"
}
