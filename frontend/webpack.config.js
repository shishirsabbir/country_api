import path from "path";
import { fileURLToPath } from "url";
import MiniCssExtractPlugin from "mini-css-extract-plugin";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default {
  // Add the 'context' property to specify the base directory for resolving entry points.
  context: __dirname,

  // Define the entry points for your JavaScript and CSS files.
  // The path has been corrected from './js/main.js' to './main.js'
  entry: {
    main: "./main.js",
    styles: "./css/main.css",
  },

  // Define where the bundled files will be saved.
  output: {
    path: path.resolve(__dirname, "../app/public/assets"),
    filename: "[name].bundle.js",
    publicPath: "/public/assets/",
  },

  // Define how different file types are handled by Webpack.
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },

  // Define the plugins to use with Webpack.
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].min.css",
    }),
  ],
};
