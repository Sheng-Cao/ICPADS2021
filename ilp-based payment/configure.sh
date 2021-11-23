docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://alice-node:7770 accounts create alice \
  --auth hi_alice \
  --ilp-address example.alice \
  --asset-code ETH \
  --asset-scale 3 \
  --ilp-over-http-incoming-token alice_password

docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://alice-node:7770 accounts create bob \
  --auth hi_alice \
  --ilp-address example.bob \
  --asset-code ETH \
  --asset-scale 3 \
  --settlement-engine-url http://alice-eth:3000 \
  --ilp-over-http-incoming-token bob_password \
  --ilp-over-http-outgoing-token alice_password \
  --ilp-over-http-url http://bob-node:7770/accounts/alice/ilp \
  --settle-threshold 100000 \
  --settle-to 0 \
  --routing-relation Peer

docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://bob-node:7770 accounts create alice \
  --auth hi_bob \
  --ilp-address example.alice \
  --asset-code ETH \
  --asset-scale 3 \
  --max-packet-amount 100000 \
  --settlement-engine-url http://bob-eth:3000 \
  --ilp-over-http-incoming-token alice_password \
  --ilp-over-http-outgoing-token bob_password \
  --ilp-over-http-url http://alice-node:7770/accounts/bob/ilp \
  --min-balance -150000 \
  --routing-relation Peer

docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://bob-node:7770 accounts create charlie \
  --auth hi_bob \
  --asset-code XRP \
  --asset-scale 3 \
  --settlement-engine-url http://bob-xrp:3001 \
  --ilp-over-http-incoming-token charlie_password \
  --ilp-over-http-outgoing-token bob_other_password \
  --ilp-over-http-url http://charlie-node:7770/accounts/bob/ilp \
  --settle-threshold 10000 \
  --settle-to -1000000 \
  --routing-relation Child

docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://charlie-node:7770 accounts create bob \
  --auth hi_charlie \
  --ilp-address example.bob \
  --asset-code XRP \
  --asset-scale 3 \
  --settlement-engine-url http://charlie-xrp:3000 \
  --ilp-over-http-incoming-token bob_other_password \
  --ilp-over-http-outgoing-token charlie_password \
  --ilp-over-http-url http://bob-node:7770/accounts/charlie/ilp \
  --min-balance -50000 \
  --routing-relation Parent

docker run --rm --network local-ilp interledgerrs/ilp-cli --node http://charlie-node:7770 accounts create charlie \
  --auth hi_charlie \
  --asset-code XRP \
  --asset-scale 3 \
  --ilp-over-http-incoming-token charlie_password
