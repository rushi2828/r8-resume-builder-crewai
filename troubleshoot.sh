#!/bin/bash

# 🚀 r8-resume-builder-crewai Troubleshooting Script
# Safely rebuilds and restarts your Docker Compose setup

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🧹 Step 1: Stopping all containers and removing orphans...${NC}"
docker-compose down --remove-orphans

echo -e "${YELLOW}🔨 Step 2: Rebuilding containers with no cache...${NC}"
docker-compose build --no-cache

echo -e "${YELLOW}🚀 Step 3: Starting up containers...${NC}"
docker-compose up

