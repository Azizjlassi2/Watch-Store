import React from 'react'

const Product = ({ product,index }) => {
  return (
    <div className='product-item' id={index}>
      <div className='product-title'>{product.title}</div>
      <div className='product-marque'>{product.marque}</div>
      <div className='product-description'>{product.description}</div>
      <div className='product-price'>{product.price}</div>
     
    </div>
  )
}

export default Product;