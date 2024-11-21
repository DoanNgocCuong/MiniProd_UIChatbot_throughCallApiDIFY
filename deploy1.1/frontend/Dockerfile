# Base image để chạy Node.js
FROM node:18-alpine 

# Tạo và set thư mục làm việc
WORKDIR /app 

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .


EXPOSE 5000

# Add configuration for serving static files
ENV PUBLIC_PATH=/public
CMD ["npm", "start"]