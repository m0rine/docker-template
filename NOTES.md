Bash param expansion, in defect dojo script:

${symbol} protects against partial tokens being expanded. 

1. Parameter Expansion: Var param --> actual value. 


-   :<symbol> synax.
-  A - gives a default for unset / null
- 



DD docker flow

1. run docker-compose.yml with docker compose up
2. It pulls the images by default, and performs configuration.
3. Services (containers) are run in the order, postgres -> valkey -> initalizer -> uswgi -> nginx

