import React ,{useEffect,useState}from 'react'
import Product from '../components/Product.jsx'

const ProductListPage = () => {
  const [products,setProduct] = useState([])

    useEffect(()=>{
      getProducts()
    },[])

  let getProducts = async() =>{
    let response = await fetch("/api/products/")
    let data = await response.json()
    setProduct(data)
  }

  return (
    <div className='product-list'>
      {products.map( (product,index) => (
        <Product  product={product}  index={index} />
      )

      )}

    </div>
   
  )
}

export default ProductListPage;